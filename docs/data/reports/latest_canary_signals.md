# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T13:52:25.151356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1479` n `12`; crypto_alt avg `-0.1881` n `230`; crypto_major avg `-0.3169` n `8`; equity avg `-0.0828` n `113`; fx avg `0.0113` n `6`; index avg `0.0005` n `25`; metal avg `-0.1213` n `20`; unknown avg `0.1062` n `784`
- 1h: commodity avg `0.2756` n `12`; crypto_alt avg `-0.1982` n `230`; crypto_major avg `-0.4959` n `8`; equity avg `-0.1683` n `113`; fx avg `0.0359` n `6`; index avg `0.0126` n `25`; metal avg `-0.1574` n `20`; unknown avg `0.1028` n `784`
- 4h: commodity avg `0.417` n `12`; crypto_alt avg `-0.0677` n `230`; crypto_major avg `-0.5278` n `8`; equity avg `-0.9632` n `113`; fx avg `0.0229` n `6`; index avg `-0.0961` n `25`; metal avg `-0.1545` n `20`; unknown avg `-0.035` n `784`
- 24h: commodity avg `0.9821` n `12`; crypto_alt avg `0.3659` n `230`; crypto_major avg `-0.8315` n `8`; equity avg `-1.1338` n `113`; fx avg `0.2599` n `6`; index avg `-0.0452` n `25`; metal avg `-0.2907` n `20`; unknown avg `58.9766` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1758`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
