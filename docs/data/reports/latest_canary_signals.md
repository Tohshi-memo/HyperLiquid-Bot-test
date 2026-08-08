# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T10:07:27.221795+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0341` n `230`; crypto_major avg `0.0569` n `8`; equity avg `0.0051` n `112`; fx avg `-0.0036` n `6`; index avg `-0.0019` n `25`; metal avg `0.0046` n `20`; unknown avg `1.2058` n `784`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `0.0707` n `230`; crypto_major avg `0.0539` n `8`; equity avg `0.0523` n `112`; fx avg `0.0004` n `6`; index avg `-0.0083` n `25`; metal avg `0.0307` n `20`; unknown avg `1.1718` n `784`
- 4h: commodity avg `0.0204` n `12`; crypto_alt avg `0.267` n `230`; crypto_major avg `0.2373` n `8`; equity avg `0.1362` n `112`; fx avg `-0.0057` n `6`; index avg `0.0091` n `25`; metal avg `0.0452` n `20`; unknown avg `1.3806` n `784`
- 24h: commodity avg `0.0601` n `12`; crypto_alt avg `0.0335` n `230`; crypto_major avg `0.1239` n `8`; equity avg `0.7931` n `112`; fx avg `-0.0172` n `6`; index avg `0.0557` n `25`; metal avg `-0.1032` n `20`; unknown avg `1.2335` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
