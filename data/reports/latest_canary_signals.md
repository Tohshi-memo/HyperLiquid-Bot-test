# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T07:52:31.633775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `13`; crypto_alt avg `-0.0399` n `239`; crypto_major avg `-0.0464` n `8`; equity avg `0.1004` n `160`; fx avg `-0.0014` n `6`; index avg `0.0059` n `27`; metal avg `-0.0083` n `20`; unknown avg `-0.0597` n `1261`
- 1h: commodity avg `0.0138` n `13`; crypto_alt avg `-0.1291` n `239`; crypto_major avg `0.1074` n `8`; equity avg `0.024` n `160`; fx avg `0.0099` n `6`; index avg `-0.0051` n `27`; metal avg `-0.1055` n `20`; unknown avg `18.9037` n `1255`
- 4h: commodity avg `-0.0422` n `13`; crypto_alt avg `0.7237` n `239`; crypto_major avg `0.6167` n `8`; equity avg `0.561` n `160`; fx avg `-0.0718` n `6`; index avg `0.0925` n `27`; metal avg `-0.0783` n `20`; unknown avg `2.0984` n `1219`
- 24h: commodity avg `-0.4582` n `13`; crypto_alt avg `3.0087` n `239`; crypto_major avg `1.5493` n `8`; equity avg `5.7747` n `160`; fx avg `0.0015` n `6`; index avg `0.6493` n `27`; metal avg `0.2941` n `20`; unknown avg `189.4684` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
