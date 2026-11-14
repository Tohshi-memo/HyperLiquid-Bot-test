# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T09:52:26.959844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `0.2621` n `239`; crypto_major avg `0.3327` n `8`; equity avg `0.0386` n `162`; fx avg `-0.0009` n `6`; index avg `0.0105` n `27`; metal avg `-0.0008` n `20`; unknown avg `41.0981` n `1258`
- 1h: commodity avg `-0.0208` n `13`; crypto_alt avg `0.4401` n `239`; crypto_major avg `0.6813` n `8`; equity avg `0.1346` n `162`; fx avg `-0.0189` n `6`; index avg `0.0092` n `27`; metal avg `0.0189` n `20`; unknown avg `43.3632` n `1200`
- 4h: commodity avg `0.0052` n `13`; crypto_alt avg `-0.6753` n `239`; crypto_major avg `0.2915` n `8`; equity avg `0.1346` n `162`; fx avg `-0.0097` n `6`; index avg `0.0118` n `27`; metal avg `0.0423` n `20`; unknown avg `44.1476` n `1166`
- 24h: commodity avg `-0.14` n `13`; crypto_alt avg `-2.4604` n `239`; crypto_major avg `-2.7467` n `8`; equity avg `-2.5279` n `162`; fx avg `-0.133` n `6`; index avg `-0.2055` n `27`; metal avg `-0.3268` n `20`; unknown avg `1.6706` n `1042`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
