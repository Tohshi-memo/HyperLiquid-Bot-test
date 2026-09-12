# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T14:14:53.385698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `12`; crypto_alt avg `0.1162` n `233`; crypto_major avg `0.069` n `8`; equity avg `0.0056` n `136`; fx avg `0.0016` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0011` n `20`; unknown avg `-0.1998` n `836`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `-0.0699` n `233`; crypto_major avg `-0.068` n `8`; equity avg `-0.0248` n `136`; fx avg `-0.0057` n `6`; index avg `0.0001` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.1275` n `836`
- 4h: commodity avg `0.0032` n `12`; crypto_alt avg `0.0133` n `233`; crypto_major avg `0.0503` n `8`; equity avg `0.0097` n `136`; fx avg `-0.0009` n `6`; index avg `-0.0006` n `26`; metal avg `0.0381` n `20`; unknown avg `0.2941` n `824`
- 24h: commodity avg `-0.0933` n `12`; crypto_alt avg `-0.639` n `233`; crypto_major avg `-1.8892` n `8`; equity avg `-0.1575` n `136`; fx avg `0.0066` n `6`; index avg `0.0595` n `26`; metal avg `-0.2665` n `20`; unknown avg `9.077` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
