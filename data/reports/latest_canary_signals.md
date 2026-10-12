# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T19:22:41.548931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `13`; crypto_alt avg `-0.1426` n `235`; crypto_major avg `-0.1025` n `8`; equity avg `0.0336` n `151`; fx avg `0.0051` n `6`; index avg `0.0077` n `26`; metal avg `-0.0018` n `20`; unknown avg `32.4398` n `1134`
- 1h: commodity avg `-0.149` n `13`; crypto_alt avg `-0.1572` n `235`; crypto_major avg `-0.1279` n `8`; equity avg `-0.0516` n `151`; fx avg `0.0012` n `6`; index avg `0.0` n `26`; metal avg `-0.0361` n `20`; unknown avg `3.4879` n `1132`
- 4h: commodity avg `-0.0957` n `13`; crypto_alt avg `-0.9195` n `235`; crypto_major avg `-0.8014` n `8`; equity avg `-0.2371` n `151`; fx avg `-0.028` n `6`; index avg `-0.0268` n `26`; metal avg `-0.019` n `20`; unknown avg `0.1601` n `1126`
- 24h: commodity avg `0.4041` n `13`; crypto_alt avg `-3.1921` n `235`; crypto_major avg `-2.1782` n `8`; equity avg `-3.4952` n `151`; fx avg `-0.1602` n `6`; index avg `-0.3465` n `26`; metal avg `-0.1901` n `20`; unknown avg `-0.1214` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2119`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.18`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1206`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0991`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
