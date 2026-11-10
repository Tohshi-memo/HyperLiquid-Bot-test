# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T07:07:25.200917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `13`; crypto_alt avg `-0.0499` n `239`; crypto_major avg `0.0649` n `8`; equity avg `-0.1271` n `160`; fx avg `0.0216` n `6`; index avg `-0.0172` n `27`; metal avg `-0.0262` n `20`; unknown avg `18.9017` n `1257`
- 1h: commodity avg `-0.0769` n `13`; crypto_alt avg `0.2975` n `239`; crypto_major avg `0.1179` n `8`; equity avg `-0.3159` n `160`; fx avg `0.0124` n `6`; index avg `-0.0361` n `27`; metal avg `-0.1027` n `20`; unknown avg `0.8903` n `1251`
- 4h: commodity avg `-0.0851` n `13`; crypto_alt avg `0.6737` n `239`; crypto_major avg `0.2373` n `8`; equity avg `-0.1954` n `160`; fx avg `-0.0899` n `6`; index avg `0.0265` n `27`; metal avg `-0.0503` n `20`; unknown avg `1.8414` n `1213`
- 24h: commodity avg `-0.5727` n `13`; crypto_alt avg `2.5601` n `239`; crypto_major avg `1.1751` n `8`; equity avg `4.7677` n `160`; fx avg `0.0383` n `6`; index avg `0.5359` n `27`; metal avg `0.2262` n `20`; unknown avg `192.5431` n `1063`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
