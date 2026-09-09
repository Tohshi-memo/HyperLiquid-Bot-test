# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T02:22:28.642867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `-0.3028` n `233`; crypto_major avg `-0.1993` n `8`; equity avg `-0.0016` n `134`; fx avg `0.0193` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.4684` n `797`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.0796` n `233`; crypto_major avg `0.0761` n `8`; equity avg `0.036` n `134`; fx avg `0.0008` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0022` n `20`; unknown avg `-0.193` n `795`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.3279` n `233`; crypto_major avg `0.1443` n `8`; equity avg `0.4509` n `134`; fx avg `0.006` n `6`; index avg `0.1026` n `26`; metal avg `0.1166` n `20`; unknown avg `0.5515` n `789`
- 24h: commodity avg `0.1594` n `12`; crypto_alt avg `-1.6039` n `232`; crypto_major avg `-0.1625` n `8`; equity avg `0.2895` n `134`; fx avg `0.0915` n `6`; index avg `-0.1668` n `26`; metal avg `-0.3706` n `20`; unknown avg `-0.0652` n `683`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
