# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T01:21:55.626260+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `-0.2629` n `233`; crypto_major avg `-0.2705` n `8`; equity avg `0.0004` n `134`; fx avg `-0.0005` n `6`; index avg `0.0043` n `26`; metal avg `-0.011` n `20`; unknown avg `0.058` n `797`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `-0.5564` n `233`; crypto_major avg `-0.2934` n `8`; equity avg `0.2407` n `134`; fx avg `0.0363` n `6`; index avg `0.0428` n `26`; metal avg `0.1242` n `20`; unknown avg `0.1907` n `789`
- 4h: commodity avg `0.0111` n `12`; crypto_alt avg `-0.1996` n `233`; crypto_major avg `0.2338` n `8`; equity avg `0.3713` n `134`; fx avg `-0.0123` n `6`; index avg `0.1057` n `26`; metal avg `0.0645` n `20`; unknown avg `0.5989` n `741`
- 24h: commodity avg `0.1465` n `12`; crypto_alt avg `-1.3147` n `232`; crypto_major avg `-0.1716` n `8`; equity avg `0.4732` n `134`; fx avg `0.0177` n `6`; index avg `-0.1137` n `26`; metal avg `-0.4069` n `20`; unknown avg `-0.1995` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
