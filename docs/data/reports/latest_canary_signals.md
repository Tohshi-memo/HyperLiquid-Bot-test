# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T10:37:25.829679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1469` n `12`; crypto_alt avg `-0.0193` n `230`; crypto_major avg `-0.0633` n `8`; equity avg `-0.0444` n `113`; fx avg `-0.0045` n `6`; index avg `-0.0125` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.0629` n `784`
- 1h: commodity avg `0.0249` n `12`; crypto_alt avg `0.0` n `230`; crypto_major avg `-0.0238` n `8`; equity avg `-0.1802` n `113`; fx avg `-0.005` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0257` n `20`; unknown avg `0.0241` n `784`
- 4h: commodity avg `0.3004` n `12`; crypto_alt avg `-0.0624` n `230`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0366` n `113`; fx avg `0.0236` n `6`; index avg `-0.0006` n `25`; metal avg `-0.1105` n `20`; unknown avg `0.0837` n `784`
- 24h: commodity avg `0.4502` n `12`; crypto_alt avg `0.9164` n `230`; crypto_major avg `-0.0749` n `8`; equity avg `-0.1581` n `113`; fx avg `0.2243` n `6`; index avg `0.0539` n `25`; metal avg `-0.1383` n `20`; unknown avg `57.025` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
