# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T11:56:09.422283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.067` n `12`; crypto_alt avg `0.0515` n `230`; crypto_major avg `0.0584` n `8`; equity avg `-0.0519` n `113`; fx avg `-0.002` n `6`; index avg `-0.0185` n `25`; metal avg `0.0099` n `20`; unknown avg `0.0114` n `784`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `0.1157` n `8`; equity avg `-0.2173` n `113`; fx avg `0.0017` n `6`; index avg `-0.0424` n `25`; metal avg `-0.0043` n `20`; unknown avg `-0.0448` n `784`
- 4h: commodity avg `0.3282` n `12`; crypto_alt avg `0.1036` n `230`; crypto_major avg `-0.0891` n `8`; equity avg `-0.4392` n `113`; fx avg `0.0124` n `6`; index avg `-0.0709` n `25`; metal avg `-0.1361` n `20`; unknown avg `-0.0575` n `784`
- 24h: commodity avg `0.6562` n `12`; crypto_alt avg `0.9644` n `230`; crypto_major avg `0.1698` n `8`; equity avg `-0.3797` n `113`; fx avg `0.2235` n `6`; index avg `0.0138` n `25`; metal avg `-0.1495` n `20`; unknown avg `57.0748` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
