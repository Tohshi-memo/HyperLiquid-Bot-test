# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T16:52:35.317444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `-0.621` n `235`; crypto_major avg `-0.3932` n `8`; equity avg `-0.2452` n `151`; fx avg `-0.001` n `6`; index avg `-0.0353` n `26`; metal avg `-0.0501` n `20`; unknown avg `0.1322` n `1134`
- 1h: commodity avg `-0.0039` n `13`; crypto_alt avg `-0.5434` n `235`; crypto_major avg `-0.3719` n `8`; equity avg `-0.3487` n `151`; fx avg `-0.0104` n `6`; index avg `-0.0392` n `26`; metal avg `-0.0492` n `20`; unknown avg `0.0607` n `1126`
- 4h: commodity avg `0.2904` n `13`; crypto_alt avg `-1.8834` n `235`; crypto_major avg `-1.0431` n `8`; equity avg `-1.8514` n `151`; fx avg `-0.0504` n `6`; index avg `-0.1225` n `26`; metal avg `-0.1143` n `20`; unknown avg `-0.5511` n `1074`
- 24h: commodity avg `0.532` n `13`; crypto_alt avg `-3.1186` n `235`; crypto_major avg `-2.2387` n `8`; equity avg `-3.4803` n `151`; fx avg `-0.1624` n `6`; index avg `-0.3346` n `26`; metal avg `-0.2048` n `20`; unknown avg `-0.0621` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2125`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1943`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1412`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0884`, n `666`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
