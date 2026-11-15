# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T18:52:26.339050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `13`; crypto_alt avg `-0.1009` n `239`; crypto_major avg `-0.0682` n `8`; equity avg `0.0016` n `162`; fx avg `-0.0049` n `6`; index avg `0.0021` n `27`; metal avg `0.0354` n `20`; unknown avg `-0.0693` n `1265`
- 1h: commodity avg `0.0187` n `13`; crypto_alt avg `-0.124` n `239`; crypto_major avg `-0.14` n `8`; equity avg `-0.0344` n `162`; fx avg `0.0245` n `6`; index avg `-0.0023` n `27`; metal avg `0.052` n `20`; unknown avg `-0.1836` n `1261`
- 4h: commodity avg `0.0392` n `13`; crypto_alt avg `-0.4385` n `239`; crypto_major avg `-0.4566` n `8`; equity avg `0.1346` n `162`; fx avg `0.0275` n `6`; index avg `0.0077` n `27`; metal avg `0.0868` n `20`; unknown avg `0.1346` n `1254`
- 24h: commodity avg `0.0636` n `13`; crypto_alt avg `-1.0224` n `239`; crypto_major avg `-0.5332` n `8`; equity avg `0.1937` n `162`; fx avg `0.0194` n `6`; index avg `0.0402` n `27`; metal avg `-0.0514` n `20`; unknown avg `0.0308` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
