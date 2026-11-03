# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T13:37:24.198784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.5493` n `13`; crypto_alt avg `0.5949` n `239`; crypto_major avg `0.5033` n `8`; equity avg `0.7625` n `157`; fx avg `-0.0266` n `6`; index avg `0.1263` n `27`; metal avg `0.2154` n `20`; unknown avg `281.6356` n `1262`
- 1h: commodity avg `-0.6207` n `13`; crypto_alt avg `0.1278` n `239`; crypto_major avg `0.1849` n `8`; equity avg `0.7585` n `157`; fx avg `-0.0174` n `6`; index avg `0.1219` n `27`; metal avg `0.2882` n `20`; unknown avg `2.7466` n `1254`
- 4h: commodity avg `-0.8479` n `13`; crypto_alt avg `1.6406` n `239`; crypto_major avg `1.1253` n `8`; equity avg `1.2636` n `157`; fx avg `-0.0262` n `6`; index avg `0.191` n `27`; metal avg `0.4433` n `20`; unknown avg `3.7125` n `1220`
- 24h: commodity avg `-0.8639` n `13`; crypto_alt avg `-0.4058` n `239`; crypto_major avg `-0.068` n `8`; equity avg `-1.9753` n `157`; fx avg `-0.0129` n `6`; index avg `-0.096` n `27`; metal avg `-0.0962` n `20`; unknown avg `0.0748` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
