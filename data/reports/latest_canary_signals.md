# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T20:52:29.667886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.0043` n `239`; crypto_major avg `0.0918` n `8`; equity avg `0.3348` n `162`; fx avg `0.0026` n `6`; index avg `0.0381` n `27`; metal avg `0.0357` n `20`; unknown avg `7.206` n `1262`
- 1h: commodity avg `0.0445` n `13`; crypto_alt avg `-0.3237` n `239`; crypto_major avg `0.0267` n `8`; equity avg `0.4587` n `162`; fx avg `0.0011` n `6`; index avg `0.0595` n `27`; metal avg `0.0374` n `20`; unknown avg `10.4639` n `1246`
- 4h: commodity avg `0.0894` n `13`; crypto_alt avg `0.181` n `239`; crypto_major avg `0.7174` n `8`; equity avg `1.373` n `162`; fx avg `-0.04` n `6`; index avg `0.1789` n `27`; metal avg `-0.0261` n `20`; unknown avg `6.9955` n `1246`
- 24h: commodity avg `-0.3257` n `13`; crypto_alt avg `-0.3867` n `239`; crypto_major avg `-1.5073` n `8`; equity avg `-1.9171` n `162`; fx avg `-0.0849` n `6`; index avg `-0.1299` n `27`; metal avg `-0.2605` n `20`; unknown avg `6.1144` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
