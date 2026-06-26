# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T03:37:28.215382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3495` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `0.3051` n `228`; crypto_major avg `0.3193` n `8`; equity avg `-0.1861` n `86`; fx avg `0.0045` n `6`; index avg `-0.0332` n `23`; metal avg `-0.0005` n `20`; unknown avg `0.6968` n `765`
- 1h: commodity avg `-0.0798` n `12`; crypto_alt avg `0.4522` n `228`; crypto_major avg `0.5078` n `8`; equity avg `-0.6857` n `86`; fx avg `0.0169` n `6`; index avg `-0.156` n `23`; metal avg `0.0618` n `20`; unknown avg `1.727` n `765`
- 4h: commodity avg `-0.1511` n `12`; crypto_alt avg `-1.5257` n `228`; crypto_major avg `-1.9591` n `8`; equity avg `-2.8048` n `86`; fx avg `0.0523` n `6`; index avg `-0.6096` n `23`; metal avg `-0.5842` n `20`; unknown avg `1.1753` n `749`
- 24h: commodity avg `0.3321` n `12`; crypto_alt avg `-2.2988` n `228`; crypto_major avg `-2.3154` n `8`; equity avg `-4.3815` n `86`; fx avg `0.0632` n `6`; index avg `-0.7031` n `23`; metal avg `0.0422` n `20`; unknown avg `0.3136` n `717`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
