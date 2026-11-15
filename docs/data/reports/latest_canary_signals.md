# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T09:37:36.754789+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `13`; crypto_alt avg `-0.2793` n `239`; crypto_major avg `-0.4007` n `8`; equity avg `-0.0336` n `162`; fx avg `0.0103` n `6`; index avg `0.0019` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.7471` n `1263`
- 1h: commodity avg `-0.0144` n `13`; crypto_alt avg `1.3842` n `239`; crypto_major avg `1.4747` n `8`; equity avg `0.3946` n `162`; fx avg `-0.0014` n `6`; index avg `0.0448` n `27`; metal avg `0.0833` n `20`; unknown avg `1.0969` n `1261`
- 4h: commodity avg `-0.0437` n `13`; crypto_alt avg `0.4832` n `239`; crypto_major avg `0.7888` n `8`; equity avg `0.2303` n `162`; fx avg `-0.0172` n `6`; index avg `0.0263` n `27`; metal avg `0.1461` n `20`; unknown avg `1.1327` n `1225`
- 24h: commodity avg `0.0394` n `13`; crypto_alt avg `-4.3493` n `239`; crypto_major avg `-3.4228` n `8`; equity avg `-0.7154` n `162`; fx avg `0.0371` n `6`; index avg `-0.0564` n `27`; metal avg `-0.3484` n `20`; unknown avg `45.034` n `1116`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
