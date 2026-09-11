# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T07:37:29.468911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `-0.149` n `233`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0376` n `136`; fx avg `-0.0176` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0235` n `20`; unknown avg `0.1355` n `796`
- 1h: commodity avg `-0.0265` n `12`; crypto_alt avg `0.1966` n `233`; crypto_major avg `0.1507` n `8`; equity avg `0.1131` n `136`; fx avg `-0.0204` n `6`; index avg `0.0016` n `26`; metal avg `-0.0238` n `20`; unknown avg `0.0784` n `792`
- 4h: commodity avg `-0.3629` n `12`; crypto_alt avg `0.7564` n `233`; crypto_major avg `0.7011` n `8`; equity avg `0.8933` n `136`; fx avg `-0.0151` n `6`; index avg `0.1833` n `26`; metal avg `0.3182` n `20`; unknown avg `42.2037` n `762`
- 24h: commodity avg `0.7695` n `12`; crypto_alt avg `-0.8645` n `233`; crypto_major avg `-1.0571` n `8`; equity avg `-1.3152` n `136`; fx avg `0.0421` n `6`; index avg `-0.2264` n `26`; metal avg `-0.951` n `20`; unknown avg `0.6122` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
