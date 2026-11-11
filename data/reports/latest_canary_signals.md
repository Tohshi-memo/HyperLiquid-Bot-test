# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T14:22:25.875788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `13`; crypto_alt avg `-0.2897` n `239`; crypto_major avg `-0.3809` n `8`; equity avg `-0.0362` n `161`; fx avg `-0.0023` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0243` n `20`; unknown avg `0.2956` n `1261`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-0.0114` n `239`; crypto_major avg `-0.2224` n `8`; equity avg `-0.2484` n `161`; fx avg `-0.008` n `6`; index avg `-0.0438` n `27`; metal avg `-0.1039` n `20`; unknown avg `38.076` n `1255`
- 4h: commodity avg `0.0845` n `13`; crypto_alt avg `0.0964` n `239`; crypto_major avg `-0.1466` n `8`; equity avg `0.2883` n `161`; fx avg `-0.0379` n `6`; index avg `0.0269` n `27`; metal avg `-0.1544` n `20`; unknown avg `0.4129` n `1247`
- 24h: commodity avg `1.1393` n `13`; crypto_alt avg `-0.2696` n `239`; crypto_major avg `-0.3991` n `8`; equity avg `4.3292` n `161`; fx avg `-0.2484` n `6`; index avg `0.3544` n `27`; metal avg `0.2577` n `20`; unknown avg `1.9827` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2797`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
