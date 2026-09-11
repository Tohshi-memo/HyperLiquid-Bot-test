# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T22:37:25.342228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.13` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.3066` n `233`; crypto_major avg `-0.3346` n `8`; equity avg `-0.0192` n `136`; fx avg `0.0027` n `6`; index avg `0.0001` n `26`; metal avg `-0.0087` n `20`; unknown avg `1.5202` n `830`
- 1h: commodity avg `0.0057` n `12`; crypto_alt avg `-0.7747` n `233`; crypto_major avg `-0.7003` n `8`; equity avg `-0.0273` n `136`; fx avg `-0.0011` n `6`; index avg `0.0064` n `26`; metal avg `-0.0215` n `20`; unknown avg `5.2035` n `820`
- 4h: commodity avg `-0.0747` n `12`; crypto_alt avg `-0.6659` n `233`; crypto_major avg `-0.5018` n `8`; equity avg `-0.1956` n `136`; fx avg `-0.0116` n `6`; index avg `-0.0231` n `26`; metal avg `0.0115` n `20`; unknown avg `0.8902` n `770`
- 24h: commodity avg `-0.79` n `12`; crypto_alt avg `-0.0524` n `233`; crypto_major avg `0.7734` n `8`; equity avg `0.8138` n `136`; fx avg `-0.1879` n `6`; index avg `0.3226` n `26`; metal avg `0.3076` n `20`; unknown avg `2.0288` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
