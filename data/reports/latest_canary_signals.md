# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T08:07:26.759103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.1999` n `237`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0021` n `151`; fx avg `-0.0147` n `6`; index avg `0.0034` n `26`; metal avg `0.0156` n `20`; unknown avg `-0.0204` n `1149`
- 1h: commodity avg `-0.0113` n `13`; crypto_alt avg `-0.1068` n `237`; crypto_major avg `-0.3476` n `8`; equity avg `-0.1483` n `151`; fx avg `-0.0185` n `6`; index avg `-0.0389` n `26`; metal avg `-0.0954` n `20`; unknown avg `0.1681` n `1146`
- 4h: commodity avg `-0.081` n `13`; crypto_alt avg `0.2247` n `237`; crypto_major avg `0.09` n `8`; equity avg `0.0003` n `151`; fx avg `-0.057` n `6`; index avg `-0.0152` n `26`; metal avg `-0.1017` n `20`; unknown avg `0.1641` n `1124`
- 24h: commodity avg `-0.5046` n `13`; crypto_alt avg `0.5743` n `237`; crypto_major avg `1.1155` n `8`; equity avg `2.656` n `151`; fx avg `-0.0696` n `6`; index avg `0.474` n `26`; metal avg `0.2365` n `20`; unknown avg `2.4714` n `875`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1948`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.143`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1218`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1041`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0627`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
