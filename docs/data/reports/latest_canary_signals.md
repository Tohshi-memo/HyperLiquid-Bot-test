# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T06:22:25.050947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `13`; crypto_alt avg `0.2224` n `239`; crypto_major avg `0.1806` n `8`; equity avg `-0.0086` n `162`; fx avg `-0.0013` n `6`; index avg `-0.0016` n `27`; metal avg `-0.0003` n `20`; unknown avg `233.7561` n `1262`
- 1h: commodity avg `0.016` n `13`; crypto_alt avg `0.3497` n `239`; crypto_major avg `0.3909` n `8`; equity avg `0.1156` n `162`; fx avg `0.0032` n `6`; index avg `0.0115` n `27`; metal avg `0.0101` n `20`; unknown avg `0.4312` n `1238`
- 4h: commodity avg `-0.0208` n `13`; crypto_alt avg `0.503` n `239`; crypto_major avg `-0.1855` n `8`; equity avg `0.1211` n `162`; fx avg `0.0004` n `6`; index avg `0.0012` n `27`; metal avg `-0.0166` n `20`; unknown avg `0.501` n `1222`
- 24h: commodity avg `-0.1174` n `13`; crypto_alt avg `-0.888` n `239`; crypto_major avg `-1.8878` n `8`; equity avg `-2.3922` n `162`; fx avg `-0.1387` n `6`; index avg `-0.1894` n `27`; metal avg `-0.4397` n `20`; unknown avg `60.239` n `1022`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
