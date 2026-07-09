# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T11:16:23.049900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0594` n `12`; crypto_alt avg `-0.0897` n `229`; crypto_major avg `-0.1581` n `8`; equity avg `-0.0293` n `91`; fx avg `0.0048` n `6`; index avg `-0.006` n `25`; metal avg `0.0145` n `20`; unknown avg `-0.0218` n `764`
- 1h: commodity avg `0.0958` n `12`; crypto_alt avg `-0.2248` n `229`; crypto_major avg `-0.442` n `8`; equity avg `-0.337` n `91`; fx avg `0.0032` n `6`; index avg `-0.0395` n `25`; metal avg `-0.019` n `20`; unknown avg `0.0121` n `764`
- 4h: commodity avg `0.0857` n `12`; crypto_alt avg `-0.1921` n `229`; crypto_major avg `-0.5565` n `8`; equity avg `-0.2037` n `91`; fx avg `0.0101` n `6`; index avg `-0.0553` n `25`; metal avg `-0.0234` n `20`; unknown avg `-0.1203` n `764`
- 24h: commodity avg `-0.3032` n `12`; crypto_alt avg `1.4392` n `229`; crypto_major avg `0.4044` n `8`; equity avg `3.1202` n `91`; fx avg `0.1323` n `6`; index avg `0.467` n `25`; metal avg `0.6632` n `20`; unknown avg `0.7346` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
