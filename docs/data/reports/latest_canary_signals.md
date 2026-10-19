# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T11:52:31.497156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `13`; crypto_alt avg `0.252` n `237`; crypto_major avg `0.2424` n `8`; equity avg `0.362` n `151`; fx avg `0.0043` n `6`; index avg `0.0253` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.8209` n `1193`
- 1h: commodity avg `-0.0156` n `13`; crypto_alt avg `-0.1457` n `237`; crypto_major avg `-0.0405` n `8`; equity avg `-0.0979` n `151`; fx avg `0.0191` n `6`; index avg `-0.0622` n `26`; metal avg `0.0193` n `20`; unknown avg `-0.0563` n `1191`
- 4h: commodity avg `0.36` n `13`; crypto_alt avg `-1.0213` n `237`; crypto_major avg `-0.5303` n `8`; equity avg `0.2179` n `151`; fx avg `0.0191` n `6`; index avg `-0.0103` n `26`; metal avg `0.0398` n `20`; unknown avg `0.2367` n `1147`
- 24h: commodity avg `-0.1814` n `13`; crypto_alt avg `-0.4426` n `237`; crypto_major avg `0.3724` n `8`; equity avg `2.7439` n `151`; fx avg `-0.0335` n `6`; index avg `0.4356` n `26`; metal avg `0.2404` n `20`; unknown avg `1.034` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1974`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1319`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0585`, n `666`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
