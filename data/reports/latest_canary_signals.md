# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T21:37:25.909983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `-0.1212` n `237`; crypto_major avg `0.0179` n `8`; equity avg `0.0046` n `151`; fx avg `-0.0008` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.1573` n `1162`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.3723` n `237`; crypto_major avg `0.5192` n `8`; equity avg `0.0816` n `151`; fx avg `-0.0332` n `6`; index avg `0.012` n `26`; metal avg `0.0203` n `20`; unknown avg `0.8301` n `1154`
- 4h: commodity avg `0.0404` n `13`; crypto_alt avg `-1.4529` n `237`; crypto_major avg `-0.4383` n `8`; equity avg `-0.1033` n `151`; fx avg `-0.0497` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0296` n `20`; unknown avg `4.1783` n `1122`
- 24h: commodity avg `0.0275` n `13`; crypto_alt avg `-2.9711` n `236`; crypto_major avg `-0.5233` n `8`; equity avg `0.5169` n `151`; fx avg `-0.0526` n `6`; index avg `0.0176` n `26`; metal avg `0.0347` n `20`; unknown avg `0.7979` n `993`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2088`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1424`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0736`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
