# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T17:22:32.101450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.94` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `0.1589` n `230`; crypto_major avg `0.084` n `8`; equity avg `0.3159` n `102`; fx avg `-0.0025` n `6`; index avg `0.0819` n `25`; metal avg `0.061` n `20`; unknown avg `0.0302` n `778`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `0.0262` n `230`; crypto_major avg `0.0237` n `8`; equity avg `1.1712` n `102`; fx avg `0.0286` n `6`; index avg `0.2241` n `25`; metal avg `0.3156` n `20`; unknown avg `0.0419` n `778`
- 4h: commodity avg `0.2542` n `12`; crypto_alt avg `-0.2958` n `230`; crypto_major avg `-0.2467` n `8`; equity avg `-1.4434` n `102`; fx avg `-0.0198` n `6`; index avg `-0.1374` n `25`; metal avg `0.2177` n `20`; unknown avg `0.2331` n `777`
- 24h: commodity avg `1.2997` n `12`; crypto_alt avg `-2.2353` n `230`; crypto_major avg `-0.3589` n `8`; equity avg `-1.5785` n `102`; fx avg `-0.0765` n `6`; index avg `-0.3189` n `25`; metal avg `-0.0101` n `20`; unknown avg `-0.1578` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
