# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T21:52:29.304387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `-0.9284` n `235`; crypto_major avg `-0.6033` n `8`; equity avg `-0.0906` n `151`; fx avg `0.0068` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0195` n `20`; unknown avg `2.2247` n `1135`
- 1h: commodity avg `0.066` n `13`; crypto_alt avg `-1.4312` n `235`; crypto_major avg `-0.9487` n `8`; equity avg `-0.1561` n `151`; fx avg `0.0008` n `6`; index avg `-0.0149` n `26`; metal avg `0.0047` n `20`; unknown avg `2.301` n `1102`
- 4h: commodity avg `-0.137` n `13`; crypto_alt avg `-1.1593` n `235`; crypto_major avg `-0.5199` n `8`; equity avg `-0.049` n `151`; fx avg `-0.0072` n `6`; index avg `-0.0185` n `26`; metal avg `0.0286` n `20`; unknown avg `2.131` n `1076`
- 24h: commodity avg `0.2522` n `13`; crypto_alt avg `-3.7319` n `235`; crypto_major avg `-2.1087` n `8`; equity avg `-3.4673` n `151`; fx avg `-0.1573` n `6`; index avg `-0.3461` n `26`; metal avg `-0.1616` n `20`; unknown avg `0.4837` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2038`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1753`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0936`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0873`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `666`, weak_sample_signal
