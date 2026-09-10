# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T22:37:37.456316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.4622` n `233`; crypto_major avg `-0.3755` n `8`; equity avg `-0.135` n `136`; fx avg `-0.0072` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0452` n `20`; unknown avg `0.4568` n `786`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `-0.4123` n `233`; crypto_major avg `-0.2932` n `8`; equity avg `-0.0869` n `136`; fx avg `0.0122` n `6`; index avg `-0.0146` n `26`; metal avg `-0.075` n `20`; unknown avg `0.1577` n `762`
- 4h: commodity avg `0.2756` n `12`; crypto_alt avg `-0.2612` n `233`; crypto_major avg `-0.0449` n `8`; equity avg `-0.4388` n `136`; fx avg `0.0333` n `6`; index avg `-0.0051` n `26`; metal avg `-0.0904` n `20`; unknown avg `-0.0693` n `718`
- 24h: commodity avg `1.1568` n `12`; crypto_alt avg `-1.487` n `233`; crypto_major avg `-1.7063` n `8`; equity avg `-2.033` n `136`; fx avg `0.1412` n `6`; index avg `-0.3367` n `26`; metal avg `-1.3079` n `20`; unknown avg `-0.9751` n `685`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
