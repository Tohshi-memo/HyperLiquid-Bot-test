# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T19:52:17.611920+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.58` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1497` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7924` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6093` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.051` n `12`; crypto_alt avg `0.0802` n `228`; crypto_major avg `0.0329` n `8`; equity avg `-0.0567` n `69`; fx avg `-0.0025` n `6`; index avg `-0.1443` n `23`; metal avg `-0.0849` n `18`; unknown avg `0.0021` n `422`
- 1h: commodity avg `-0.2222` n `12`; crypto_alt avg `0.4304` n `228`; crypto_major avg `0.3145` n `8`; equity avg `-0.462` n `69`; fx avg `-0.0127` n `6`; index avg `-0.1753` n `23`; metal avg `-0.2487` n `18`; unknown avg `0.0021` n `422`
- 4h: commodity avg `-0.4885` n `12`; crypto_alt avg `2.1212` n `228`; crypto_major avg `1.6612` n `8`; equity avg `-0.1312` n `69`; fx avg `0.0523` n `6`; index avg `0.3432` n `23`; metal avg `0.0519` n `18`; unknown avg `0.266` n `422`
- 24h: commodity avg `0.3535` n `12`; crypto_alt avg `2.0977` n `228`; crypto_major avg `0.1155` n `8`; equity avg `-0.055` n `69`; fx avg `0.0451` n `6`; index avg `0.253` n `23`; metal avg `-0.0436` n `18`; unknown avg `3.3443` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
