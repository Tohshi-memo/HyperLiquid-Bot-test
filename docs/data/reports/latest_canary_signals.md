# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T20:22:28.025727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0808` n `12`; crypto_alt avg `-0.2691` n `230`; crypto_major avg `-0.282` n `8`; equity avg `-0.0857` n `92`; fx avg `-0.0072` n `6`; index avg `-0.0343` n `25`; metal avg `-0.0513` n `20`; unknown avg `-0.0702` n `766`
- 1h: commodity avg `0.1029` n `12`; crypto_alt avg `0.0212` n `230`; crypto_major avg `0.0219` n `8`; equity avg `0.1038` n `92`; fx avg `0.0002` n `6`; index avg `-0.0218` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0919` n `766`
- 4h: commodity avg `0.6242` n `12`; crypto_alt avg `-0.801` n `230`; crypto_major avg `-0.3794` n `8`; equity avg `-0.5848` n `92`; fx avg `-0.01` n `6`; index avg `-0.1106` n `25`; metal avg `-0.1597` n `20`; unknown avg `-0.3233` n `766`
- 24h: commodity avg `0.6841` n `12`; crypto_alt avg `-2.4884` n `230`; crypto_major avg `-3.1343` n `8`; equity avg `-3.3485` n `92`; fx avg `-0.0761` n `6`; index avg `-0.6705` n `25`; metal avg `-0.5592` n `20`; unknown avg `-0.306` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1764`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
