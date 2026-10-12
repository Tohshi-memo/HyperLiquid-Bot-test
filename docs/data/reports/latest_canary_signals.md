# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T21:07:28.003218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `13`; crypto_alt avg `-0.3723` n `235`; crypto_major avg `-0.3572` n `8`; equity avg `-0.0236` n `151`; fx avg `-0.0037` n `6`; index avg `-0.0182` n `26`; metal avg `0.0192` n `20`; unknown avg `0.3016` n `1104`
- 1h: commodity avg `-0.0439` n `13`; crypto_alt avg `-0.3342` n `235`; crypto_major avg `-0.3453` n `8`; equity avg `-0.0241` n `151`; fx avg `-0.0062` n `6`; index avg `-0.0206` n `26`; metal avg `0.0464` n `20`; unknown avg `0.4025` n `1104`
- 4h: commodity avg `-0.1994` n `13`; crypto_alt avg `0.0058` n `235`; crypto_major avg `0.0097` n `8`; equity avg `-0.0066` n `151`; fx avg `-0.0104` n `6`; index avg `-0.031` n `26`; metal avg `0.0453` n `20`; unknown avg `0.6419` n `1078`
- 24h: commodity avg `0.1765` n `13`; crypto_alt avg `-2.8274` n `235`; crypto_major avg `-1.7325` n `8`; equity avg `-3.3627` n `151`; fx avg `-0.1548` n `6`; index avg `-0.3534` n `26`; metal avg `-0.138` n `20`; unknown avg `3.4487` n `885`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2078`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1757`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0957`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0886`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `666`, weak_sample_signal
