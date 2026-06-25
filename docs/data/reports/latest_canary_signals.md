# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T20:37:29.730791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0528` n `12`; crypto_alt avg `-0.0422` n `228`; crypto_major avg `-0.161` n `8`; equity avg `-0.1395` n `86`; fx avg `0.0015` n `6`; index avg `-0.0319` n `23`; metal avg `-0.0327` n `20`; unknown avg `-0.0461` n `765`
- 1h: commodity avg `-0.089` n `12`; crypto_alt avg `0.6662` n `228`; crypto_major avg `0.5903` n `8`; equity avg `0.4727` n `86`; fx avg `-0.0075` n `6`; index avg `0.0768` n `23`; metal avg `-0.0548` n `20`; unknown avg `0.2634` n `765`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `0.1989` n `228`; crypto_major avg `0.5708` n `8`; equity avg `0.2259` n `86`; fx avg `0.0105` n `6`; index avg `0.0258` n `23`; metal avg `-0.1213` n `20`; unknown avg `0.2404` n `765`
- 24h: commodity avg `0.4469` n `12`; crypto_alt avg `-1.2742` n `228`; crypto_major avg `-1.3628` n `8`; equity avg `-1.6282` n `86`; fx avg `0.089` n `6`; index avg `-0.0188` n `23`; metal avg `0.3337` n `20`; unknown avg `0.2953` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
