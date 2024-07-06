/*!
 * Color mode toggler for Bootstrap's docs (https://getbootstrap.com/)
 * Copyright 2011-2024 The Bootstrap Authors
 * Licensed under the Creative Commons Attribution 3.0 Unported License.
 */

(() => {
  'use strict'

  const getStoredTheme = () => localStorage.getItem('theme')
  const setStoredTheme = theme => localStorage.setItem('theme', theme)
  const getStoredDirection = () => localStorage.getItem('direction')
  const setStoredDirection = direction => localStorage.setItem('direction', direction)

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme()
    if (storedTheme) {
      return storedTheme
    }

    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
  }

  const setTheme = theme => {
    if (theme === 'auto') {
      document.documentElement.setAttribute('data-bs-theme', (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'))
    } else {
      document.documentElement.setAttribute('data-bs-theme', theme)
    }
  }

  setTheme(getPreferredTheme())

  const getPreferredDirection = () => {
    const storedDirection = getStoredDirection()
    return storedDirection || 'ltr'
  }

  const setDirection = direction => {
    document.documentElement.setAttribute('dir', direction)
  }

  setDirection(getPreferredDirection())

  const showActiveTheme = (theme, focus = false) => {
    const themeSwitcher = document.querySelector('#bd-theme')

    if (!themeSwitcher) {
      return
    }

    const themeSwitcherText = document.querySelector('#bd-theme-text')
    const activeThemeIcon = document.querySelector('.theme-icon-active use')
    const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
    const svgOfActiveBtn = btnToActive.querySelector('svg use').getAttribute('href')

    document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
      element.classList.remove('active')
      element.setAttribute('aria-pressed', 'false')
    })

    btnToActive.classList.add('active')
    btnToActive.setAttribute('aria-pressed', 'true')
    activeThemeIcon.setAttribute('href', svgOfActiveBtn)
    const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
    themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)

    if (focus) {
      themeSwitcher.focus()
    }
  }

  const showActiveDirection = (direction, focus = false) => {
    const directionSwitcher = document.querySelector('#bd-direction')

    if (!directionSwitcher) {
      return
    }

    const directionSwitcherText = document.querySelector('#bd-direction-text')

    document.querySelectorAll('[data-bs-direction-value]').forEach(element => {
      element.classList.remove('active')
      element.setAttribute('aria-pressed', 'false')
    })

    const btnToActive = document.querySelector(`[data-bs-direction-value="${direction}"]`)
    btnToActive.classList.add('active')
    btnToActive.setAttribute('aria-pressed', 'true')
    directionSwitcherText.textContent = direction.toUpperCase()

    if (focus) {
      directionSwitcher.focus()
    }
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    const storedTheme = getStoredTheme()
    if (storedTheme !== 'light' && storedTheme !== 'dark') {
      setTheme(getPreferredTheme())
    }
  })

  window.addEventListener('DOMContentLoaded', () => {
    showActiveTheme(getPreferredTheme())
    showActiveDirection(getPreferredDirection())

    document.querySelectorAll('[data-bs-theme-value]')
      .forEach(toggle => {
        toggle.addEventListener('click', () => {
          const theme = toggle.getAttribute('data-bs-theme-value')
          setStoredTheme(theme)
          setTheme(theme)
          showActiveTheme(theme, true)
        })
      })

    document.querySelectorAll('[data-bs-direction-value]')
      .forEach(toggle => {
        toggle.addEventListener('click', () => {
          const direction = toggle.getAttribute('data-bs-direction-value')
          setStoredDirection(direction)
          setDirection(direction)
          showActiveDirection(direction, true)
        })
      })
  })
})()