# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T08:22:28.736721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `12`; crypto_alt avg `0.1408` n `233`; crypto_major avg `0.1284` n `8`; equity avg `0.0786` n `136`; fx avg `-0.008` n `6`; index avg `0.0237` n `26`; metal avg `-0.0033` n `20`; unknown avg `1.2805` n `796`
- 1h: commodity avg `-0.0364` n `12`; crypto_alt avg `-0.2987` n `233`; crypto_major avg `-0.1801` n `8`; equity avg `-0.0841` n `136`; fx avg `-0.0129` n `6`; index avg `-0.004` n `26`; metal avg `-0.0268` n `20`; unknown avg `-0.0901` n `794`
- 4h: commodity avg `-0.3257` n `12`; crypto_alt avg `-0.085` n `233`; crypto_major avg `0.2998` n `8`; equity avg `0.704` n `136`; fx avg `0.0227` n `6`; index avg `0.1478` n `26`; metal avg `0.2155` n `20`; unknown avg `19.1406` n `762`
- 24h: commodity avg `0.6723` n `12`; crypto_alt avg `-1.1119` n `233`; crypto_major avg `-1.4387` n `8`; equity avg `-1.2959` n `136`; fx avg `0.0187` n `6`; index avg `-0.2085` n `26`; metal avg `-0.9527` n `20`; unknown avg `1.4565` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
