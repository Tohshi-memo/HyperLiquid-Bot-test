# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T09:52:32.447401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.0352` n `233`; crypto_major avg `0.082` n `8`; equity avg `0.0383` n `136`; fx avg `-0.0148` n `6`; index avg `0.0053` n `26`; metal avg `0.0158` n `20`; unknown avg `-0.0482` n `796`
- 1h: commodity avg `-0.0964` n `12`; crypto_alt avg `-0.5898` n `233`; crypto_major avg `-0.4659` n `8`; equity avg `-0.0783` n `136`; fx avg `-0.0263` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0574` n `20`; unknown avg `-0.2513` n `794`
- 4h: commodity avg `-0.304` n `12`; crypto_alt avg `-0.6086` n `233`; crypto_major avg `-0.2726` n `8`; equity avg `0.4335` n `136`; fx avg `-0.0555` n `6`; index avg `0.0942` n `26`; metal avg `0.0289` n `20`; unknown avg `0.2324` n `762`
- 24h: commodity avg `0.2674` n `12`; crypto_alt avg `-1.3014` n `233`; crypto_major avg `-1.4135` n `8`; equity avg `-0.8829` n `136`; fx avg `-0.0546` n `6`; index avg `-0.1192` n `26`; metal avg `-0.8425` n `20`; unknown avg `1.3938` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
