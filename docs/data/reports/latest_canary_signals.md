# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T08:37:26.971469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1221` n `12`; crypto_alt avg `0.1536` n `233`; crypto_major avg `0.2074` n `8`; equity avg `0.2677` n `136`; fx avg `-0.0444` n `6`; index avg `0.0521` n `26`; metal avg `0.0728` n `20`; unknown avg `4.895` n `790`
- 1h: commodity avg `-0.1855` n `12`; crypto_alt avg `0.0025` n `233`; crypto_major avg `0.1175` n `8`; equity avg `0.221` n `136`; fx avg `-0.0398` n `6`; index avg `0.0655` n `26`; metal avg `0.0694` n `20`; unknown avg `4.7993` n `788`
- 4h: commodity avg `-0.4759` n `12`; crypto_alt avg `-0.0324` n `233`; crypto_major avg `0.3635` n `8`; equity avg `0.7859` n `136`; fx avg `-0.0241` n `6`; index avg `0.1465` n `26`; metal avg `0.2578` n `20`; unknown avg `6.4517` n `762`
- 24h: commodity avg `0.4917` n `12`; crypto_alt avg `-0.9882` n `233`; crypto_major avg `-1.2294` n `8`; equity avg `-1.0026` n `136`; fx avg `-0.0385` n `6`; index avg `-0.1494` n `26`; metal avg `-0.8352` n `20`; unknown avg `3.7286` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
