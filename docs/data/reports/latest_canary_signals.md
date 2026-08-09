# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T06:07:22.591507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.1251` n `230`; crypto_major avg `0.1066` n `8`; equity avg `0.0609` n `112`; fx avg `0.0` n `6`; index avg `0.0004` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0285` n `752`
- 1h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.1176` n `230`; crypto_major avg `0.0138` n `8`; equity avg `0.0679` n `112`; fx avg `-0.0087` n `6`; index avg `-0.0095` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0156` n `752`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `0.2052` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `0.0434` n `112`; fx avg `-0.0038` n `6`; index avg `0.0049` n `25`; metal avg `0.016` n `20`; unknown avg `-0.0094` n `752`
- 24h: commodity avg `0.2749` n `12`; crypto_alt avg `1.5354` n `230`; crypto_major avg `0.4908` n `8`; equity avg `0.6783` n `112`; fx avg `-0.0145` n `6`; index avg `0.0771` n `25`; metal avg `0.0318` n `20`; unknown avg `-0.013` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.045`, n `668`, weak_sample_signal
