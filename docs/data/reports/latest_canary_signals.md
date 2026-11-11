# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T06:37:33.990539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0463` n `13`; crypto_alt avg `0.0105` n `239`; crypto_major avg `-0.0027` n `8`; equity avg `0.1422` n `161`; fx avg `-0.0165` n `6`; index avg `0.0245` n `27`; metal avg `-0.0147` n `20`; unknown avg `199.0138` n `1257`
- 1h: commodity avg `0.1528` n `13`; crypto_alt avg `-0.3286` n `239`; crypto_major avg `0.0135` n `8`; equity avg `0.3782` n `161`; fx avg `-0.0195` n `6`; index avg `0.0299` n `27`; metal avg `-0.0065` n `20`; unknown avg `41.1227` n `1221`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `-0.4282` n `239`; crypto_major avg `0.2202` n `8`; equity avg `1.2598` n `161`; fx avg `-0.0746` n `6`; index avg `0.1648` n `27`; metal avg `0.1833` n `20`; unknown avg `1.7989` n `1213`
- 24h: commodity avg `0.3963` n `13`; crypto_alt avg `-1.08` n `239`; crypto_major avg `-2.1486` n `8`; equity avg `1.9539` n `161`; fx avg `-0.2082` n `6`; index avg `0.2411` n `27`; metal avg `-0.1115` n `20`; unknown avg `2.2854` n `1160`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
