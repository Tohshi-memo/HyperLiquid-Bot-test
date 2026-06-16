# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T12:22:39.296905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0568` n `12`; crypto_alt avg `0.2585` n `228`; crypto_major avg `0.4714` n `8`; equity avg `-0.2261` n `77`; fx avg `-0.0092` n `6`; index avg `-0.1157` n `23`; metal avg `-0.1995` n `18`; unknown avg `0.1378` n `687`
- 1h: commodity avg `-0.3057` n `12`; crypto_alt avg `0.1976` n `228`; crypto_major avg `0.4215` n `8`; equity avg `-0.4571` n `77`; fx avg `-0.0356` n `6`; index avg `-0.1123` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.0052` n `687`
- 4h: commodity avg `-0.1787` n `12`; crypto_alt avg `0.5372` n `228`; crypto_major avg `1.1398` n `8`; equity avg `-0.1889` n `77`; fx avg `-0.0032` n `6`; index avg `-0.0284` n `23`; metal avg `0.2238` n `18`; unknown avg `0.564` n `687`
- 24h: commodity avg `-0.4145` n `12`; crypto_alt avg `0.4491` n `228`; crypto_major avg `2.3073` n `8`; equity avg `1.5467` n `76`; fx avg `-0.0853` n `6`; index avg `0.4534` n `23`; metal avg `0.1576` n `18`; unknown avg `0.444` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
