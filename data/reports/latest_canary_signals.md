# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T06:52:29.032836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `-0.0487` n `230`; crypto_major avg `-0.1339` n `8`; equity avg `-0.0222` n `93`; fx avg `0.0118` n `6`; index avg `-0.0039` n `25`; metal avg `0.0175` n `20`; unknown avg `0.0169` n `767`
- 1h: commodity avg `0.0053` n `12`; crypto_alt avg `0.2524` n `230`; crypto_major avg `0.2568` n `8`; equity avg `0.0297` n `93`; fx avg `0.0212` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.1062` n `749`
- 4h: commodity avg `-0.1472` n `12`; crypto_alt avg `0.4544` n `230`; crypto_major avg `0.7956` n `8`; equity avg `0.0636` n `93`; fx avg `-0.0007` n `6`; index avg `0.0126` n `25`; metal avg `-0.0661` n `20`; unknown avg `0.1523` n `749`
- 24h: commodity avg `-0.0442` n `12`; crypto_alt avg `1.6752` n `230`; crypto_major avg `3.4331` n `8`; equity avg `1.7579` n `92`; fx avg `0.0605` n `6`; index avg `0.4957` n `25`; metal avg `0.1995` n `20`; unknown avg `0.2663` n `740`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
