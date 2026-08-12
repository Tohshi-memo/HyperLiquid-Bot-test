# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T13:07:40.290346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0835` n `12`; crypto_alt avg `0.0083` n `230`; crypto_major avg `0.1528` n `8`; equity avg `0.0866` n `113`; fx avg `-0.0373` n `6`; index avg `0.0419` n `25`; metal avg `-0.0152` n `20`; unknown avg `-0.0397` n `786`
- 1h: commodity avg `-0.1437` n `12`; crypto_alt avg `0.0355` n `230`; crypto_major avg `-0.1949` n `8`; equity avg `0.5695` n `113`; fx avg `-0.0373` n `6`; index avg `0.1195` n `25`; metal avg `0.0341` n `20`; unknown avg `-0.0782` n `786`
- 4h: commodity avg `-0.1024` n `12`; crypto_alt avg `0.5773` n `230`; crypto_major avg `0.5579` n `8`; equity avg `0.9157` n `113`; fx avg `-0.0298` n `6`; index avg `0.158` n `25`; metal avg `0.1466` n `20`; unknown avg `-0.0678` n `786`
- 24h: commodity avg `0.2182` n `12`; crypto_alt avg `-0.7443` n `230`; crypto_major avg `0.8104` n `8`; equity avg `2.9515` n `113`; fx avg `0.0233` n `6`; index avg `0.3199` n `25`; metal avg `0.2944` n `20`; unknown avg `-0.1321` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2457`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2325`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2117`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
