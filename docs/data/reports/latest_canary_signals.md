# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T13:22:31.793149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.1184` n `230`; crypto_major avg `-0.1757` n `8`; equity avg `-0.0635` n `102`; fx avg `0.0075` n `6`; index avg `-0.009` n `25`; metal avg `0.0527` n `20`; unknown avg `0.0383` n `774`
- 1h: commodity avg `0.1136` n `12`; crypto_alt avg `-0.0554` n `230`; crypto_major avg `0.0262` n `8`; equity avg `-0.0115` n `102`; fx avg `0.0073` n `6`; index avg `0.0161` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0028` n `774`
- 4h: commodity avg `0.3578` n `12`; crypto_alt avg `-0.0612` n `230`; crypto_major avg `-0.1038` n `8`; equity avg `-0.4755` n `102`; fx avg `-0.0201` n `6`; index avg `-0.0638` n `25`; metal avg `-0.0809` n `20`; unknown avg `-0.0535` n `773`
- 24h: commodity avg `-0.3789` n `12`; crypto_alt avg `0.3741` n `230`; crypto_major avg `1.0043` n `8`; equity avg `0.7181` n `102`; fx avg `0.0797` n `6`; index avg `0.0834` n `25`; metal avg `0.2652` n `20`; unknown avg `-0.0738` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
