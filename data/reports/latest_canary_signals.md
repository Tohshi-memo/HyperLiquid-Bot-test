# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T08:07:30.633416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.021` n `13`; crypto_alt avg `0.1898` n `239`; crypto_major avg `0.2644` n `8`; equity avg `0.0723` n `162`; fx avg `0.0052` n `6`; index avg `0.01` n `27`; metal avg `0.0124` n `20`; unknown avg `0.1554` n `1240`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `-0.3426` n `239`; crypto_major avg `-0.2601` n `8`; equity avg `0.0123` n `162`; fx avg `0.0059` n `6`; index avg `0.0095` n `27`; metal avg `0.0064` n `20`; unknown avg `-0.0097` n `1240`
- 4h: commodity avg `0.0443` n `13`; crypto_alt avg `-0.3438` n `239`; crypto_major avg `0.4257` n `8`; equity avg `0.162` n `162`; fx avg `0.0033` n `6`; index avg `0.0181` n `27`; metal avg `0.0579` n `20`; unknown avg `1.1189` n `1206`
- 24h: commodity avg `-0.1632` n `13`; crypto_alt avg `-2.856` n `239`; crypto_major avg `-2.7615` n `8`; equity avg `-2.5486` n `162`; fx avg `-0.1531` n `6`; index avg `-0.2076` n `27`; metal avg `-0.3553` n `20`; unknown avg `58.1236` n `1050`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
