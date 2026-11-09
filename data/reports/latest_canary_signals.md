# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T20:52:30.339084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `13`; crypto_alt avg `0.0088` n `239`; crypto_major avg `0.1983` n `8`; equity avg `-0.3751` n `160`; fx avg `0.012` n `6`; index avg `-0.0264` n `27`; metal avg `-0.0407` n `20`; unknown avg `-0.0238` n `1261`
- 1h: commodity avg `0.3256` n `13`; crypto_alt avg `-0.1929` n `239`; crypto_major avg `0.1123` n `8`; equity avg `0.1112` n `160`; fx avg `0.0196` n `6`; index avg `0.0432` n `27`; metal avg `0.0571` n `20`; unknown avg `5.236` n `1247`
- 4h: commodity avg `-0.1754` n `13`; crypto_alt avg `-0.1669` n `239`; crypto_major avg `-0.0528` n `8`; equity avg `0.0194` n `160`; fx avg `-0.0121` n `6`; index avg `0.0998` n `27`; metal avg `0.2951` n `20`; unknown avg `3.7383` n `1245`
- 24h: commodity avg `-0.3352` n `13`; crypto_alt avg `0.5525` n `239`; crypto_major avg `-2.1345` n `8`; equity avg `4.2655` n `160`; fx avg `-0.1404` n `6`; index avg `0.5758` n `27`; metal avg `0.6664` n `20`; unknown avg `9.0293` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
