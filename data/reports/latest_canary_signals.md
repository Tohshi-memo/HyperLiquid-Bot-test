# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T12:37:27.588311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.0702` n `239`; crypto_major avg `0.1581` n `8`; equity avg `-0.0008` n `162`; fx avg `-0.0074` n `6`; index avg `0.0024` n `27`; metal avg `0.0011` n `20`; unknown avg `-0.0099` n `1262`
- 1h: commodity avg `0.0038` n `13`; crypto_alt avg `0.0732` n `239`; crypto_major avg `0.1122` n `8`; equity avg `-0.0065` n `162`; fx avg `0.0047` n `6`; index avg `0.0033` n `27`; metal avg `0.0037` n `20`; unknown avg `2.015` n `1254`
- 4h: commodity avg `-0.0635` n `13`; crypto_alt avg `-0.0834` n `239`; crypto_major avg `0.2758` n `8`; equity avg `-0.0152` n `162`; fx avg `-0.1684` n `6`; index avg `-0.0004` n `27`; metal avg `0.0184` n `20`; unknown avg `140.788` n `1177`
- 24h: commodity avg `-0.293` n `13`; crypto_alt avg `-3.5007` n `239`; crypto_major avg `-3.6633` n `8`; equity avg `-2.8267` n `162`; fx avg `-0.1378` n `6`; index avg `-0.2486` n `27`; metal avg `-0.3722` n `20`; unknown avg `1.6735` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
