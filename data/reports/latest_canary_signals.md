# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T19:52:34.272214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3458` n `13`; crypto_alt avg `0.1361` n `239`; crypto_major avg `0.2509` n `8`; equity avg `0.1532` n `160`; fx avg `-0.0213` n `6`; index avg `0.0093` n `27`; metal avg `0.0984` n `20`; unknown avg `-0.0878` n `1259`
- 1h: commodity avg `-0.5507` n `13`; crypto_alt avg `0.2114` n `239`; crypto_major avg `0.2705` n `8`; equity avg `0.0918` n `160`; fx avg `-0.0382` n `6`; index avg `0.0254` n `27`; metal avg `0.1801` n `20`; unknown avg `19.1045` n `1253`
- 4h: commodity avg `-0.5211` n `13`; crypto_alt avg `-0.8477` n `239`; crypto_major avg `-0.8629` n `8`; equity avg `-0.0971` n `160`; fx avg `-0.0251` n `6`; index avg `0.0588` n `27`; metal avg `0.148` n `20`; unknown avg `-0.3233` n `1247`
- 24h: commodity avg `-0.6078` n `13`; crypto_alt avg `0.4372` n `239`; crypto_major avg `-2.464` n `8`; equity avg `3.515` n `160`; fx avg `-0.1647` n `6`; index avg `0.4513` n `27`; metal avg `0.5916` n `20`; unknown avg `5.5499` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
