# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T15:52:41.170489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.084` n `13`; crypto_alt avg `-0.2714` n `235`; crypto_major avg `0.008` n `8`; equity avg `0.0943` n `151`; fx avg `0.0068` n `6`; index avg `0.0045` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.2082` n `1135`
- 1h: commodity avg `0.1863` n `13`; crypto_alt avg `-0.8575` n `235`; crypto_major avg `-0.4907` n `8`; equity avg `-0.154` n `151`; fx avg `0.0006` n `6`; index avg `-0.0428` n `26`; metal avg `-0.0967` n `20`; unknown avg `0.2578` n `1129`
- 4h: commodity avg `0.7703` n `13`; crypto_alt avg `0.2667` n `235`; crypto_major avg `0.176` n `8`; equity avg `-0.3011` n `151`; fx avg `0.0472` n `6`; index avg `-0.0403` n `26`; metal avg `-0.3252` n `20`; unknown avg `0.3675` n `1091`
- 24h: commodity avg `0.4656` n `13`; crypto_alt avg `-2.6781` n `235`; crypto_major avg `-1.0653` n `8`; equity avg `-1.7886` n `151`; fx avg `0.1547` n `6`; index avg `-0.3194` n `26`; metal avg `-0.2346` n `20`; unknown avg `-0.1931` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1648`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1496`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1346`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0932`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
