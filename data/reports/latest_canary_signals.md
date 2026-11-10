# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T22:37:26.499559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `-0.2134` n `239`; crypto_major avg `-0.2387` n `8`; equity avg `0.1596` n `160`; fx avg `0.0006` n `6`; index avg `0.0043` n `27`; metal avg `-0.0037` n `20`; unknown avg `-0.0497` n `1262`
- 1h: commodity avg `-0.0053` n `13`; crypto_alt avg `0.0919` n `239`; crypto_major avg `-0.2708` n `8`; equity avg `-0.0092` n `160`; fx avg `-0.0034` n `6`; index avg `-0.0183` n `27`; metal avg `0.017` n `20`; unknown avg `1.0189` n `1250`
- 4h: commodity avg `0.1377` n `13`; crypto_alt avg `-0.1645` n `239`; crypto_major avg `0.1296` n `8`; equity avg `0.9689` n `160`; fx avg `0.0067` n `6`; index avg `0.0792` n `27`; metal avg `0.044` n `20`; unknown avg `20.2838` n `1226`
- 24h: commodity avg `0.0991` n `13`; crypto_alt avg `-1.5348` n `239`; crypto_major avg `-2.9916` n `8`; equity avg `-1.3155` n `160`; fx avg `-0.0859` n `6`; index avg `-0.2043` n `27`; metal avg `-0.6588` n `20`; unknown avg `21.029` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2567`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
