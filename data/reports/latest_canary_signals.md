# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T20:22:31.933465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.0971` n `239`; crypto_major avg `0.0327` n `8`; equity avg `0.0274` n `162`; fx avg `0.0098` n `6`; index avg `0.0041` n `27`; metal avg `0.0037` n `20`; unknown avg `0.0636` n `1263`
- 1h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.0872` n `239`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0355` n `162`; fx avg `0.0362` n `6`; index avg `-0.0131` n `27`; metal avg `0.0384` n `20`; unknown avg `-0.022` n `1255`
- 4h: commodity avg `0.0645` n `13`; crypto_alt avg `0.2136` n `239`; crypto_major avg `0.4973` n `8`; equity avg `0.3925` n `162`; fx avg `0.0628` n `6`; index avg `0.0231` n `27`; metal avg `0.0907` n `20`; unknown avg `164.7035` n `1253`
- 24h: commodity avg `0.087` n `13`; crypto_alt avg `0.6477` n `239`; crypto_major avg `0.479` n `8`; equity avg `0.6035` n `162`; fx avg `0.0451` n `6`; index avg `0.0737` n `27`; metal avg `-0.009` n `20`; unknown avg `46.6482` n `1144`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
