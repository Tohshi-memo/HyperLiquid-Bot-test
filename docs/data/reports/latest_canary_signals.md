# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T06:07:26.988799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `0.0558` n `235`; crypto_major avg `0.0672` n `8`; equity avg `-0.171` n `151`; fx avg `0.0052` n `6`; index avg `-0.0751` n `26`; metal avg `-0.0429` n `20`; unknown avg `0.0841` n `1117`
- 1h: commodity avg `-0.0125` n `13`; crypto_alt avg `-0.5915` n `235`; crypto_major avg `-0.2486` n `8`; equity avg `-0.6144` n `151`; fx avg `0.0341` n `6`; index avg `-0.1538` n `26`; metal avg `-0.103` n `20`; unknown avg `0.1959` n `1117`
- 4h: commodity avg `-0.1564` n `13`; crypto_alt avg `-0.6669` n `235`; crypto_major avg `-0.2408` n `8`; equity avg `-0.909` n `151`; fx avg `0.0224` n `6`; index avg `-0.1705` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.237` n `1111`
- 24h: commodity avg `0.9784` n `13`; crypto_alt avg `-1.1042` n `235`; crypto_major avg `-0.521` n `8`; equity avg `-0.2749` n `151`; fx avg `0.0376` n `6`; index avg `-0.0137` n `26`; metal avg `-0.4112` n `20`; unknown avg `0.1462` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1559`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1384`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `666`, weak_sample_signal
