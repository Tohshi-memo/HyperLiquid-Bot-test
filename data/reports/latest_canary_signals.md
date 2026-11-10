# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T20:37:33.114647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.4586` n `239`; crypto_major avg `-0.3082` n `8`; equity avg `-0.1241` n `160`; fx avg `0.0026` n `6`; index avg `-0.0166` n `27`; metal avg `-0.0197` n `20`; unknown avg `0.648` n `1262`
- 1h: commodity avg `0.113` n `13`; crypto_alt avg `0.1308` n `239`; crypto_major avg `0.2541` n `8`; equity avg `0.4351` n `160`; fx avg `0.0021` n `6`; index avg `0.0229` n `27`; metal avg `0.0528` n `20`; unknown avg `21.0628` n `1248`
- 4h: commodity avg `0.1866` n `13`; crypto_alt avg `0.2208` n `239`; crypto_major avg `1.0619` n `8`; equity avg `-0.0328` n `160`; fx avg `0.0467` n `6`; index avg `-0.0164` n `27`; metal avg `0.1341` n `20`; unknown avg `19.1214` n `1248`
- 24h: commodity avg `0.0994` n `13`; crypto_alt avg `-2.0033` n `239`; crypto_major avg `-2.8058` n `8`; equity avg `-2.0653` n `160`; fx avg `-0.0639` n `6`; index avg `-0.2555` n `27`; metal avg `-0.693` n `20`; unknown avg `0.155` n `1161`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2567`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
