# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T23:15:33.212714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.3578` n `233`; crypto_major avg `-0.1741` n `8`; equity avg `-0.0169` n `136`; fx avg `0.0014` n `6`; index avg `0.0015` n `26`; metal avg `0.0152` n `20`; unknown avg `-0.1417` n `796`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `-1.2023` n `233`; crypto_major avg `-0.9829` n `8`; equity avg `-0.2303` n `136`; fx avg `0.0032` n `6`; index avg `-0.0207` n `26`; metal avg `-0.0032` n `20`; unknown avg `-0.0758` n `776`
- 4h: commodity avg `0.1557` n `12`; crypto_alt avg `-1.1484` n `233`; crypto_major avg `-0.923` n `8`; equity avg `-0.4399` n `136`; fx avg `0.0251` n `6`; index avg `0.0001` n `26`; metal avg `-0.0193` n `20`; unknown avg `-0.0559` n `716`
- 24h: commodity avg `1.0764` n `12`; crypto_alt avg `-2.6325` n `233`; crypto_major avg `-2.4372` n `8`; equity avg `-2.1361` n `136`; fx avg `0.1479` n `6`; index avg `-0.341` n `26`; metal avg `-1.2927` n `20`; unknown avg `-0.8015` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
