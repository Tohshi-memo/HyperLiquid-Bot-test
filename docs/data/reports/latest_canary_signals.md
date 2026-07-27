# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T13:52:28.646413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1259` n `230`; crypto_major avg `0.027` n `8`; equity avg `-0.4284` n `102`; fx avg `-0.001` n `6`; index avg `-0.0901` n `25`; metal avg `0.0603` n `20`; unknown avg `0.3133` n `774`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `0.226` n `230`; crypto_major avg `0.3402` n `8`; equity avg `-0.518` n `102`; fx avg `0.003` n `6`; index avg `-0.1439` n `25`; metal avg `0.0352` n `20`; unknown avg `0.5359` n `774`
- 4h: commodity avg `0.4191` n `12`; crypto_alt avg `0.0399` n `230`; crypto_major avg `0.1696` n `8`; equity avg `-0.9771` n `102`; fx avg `-0.0121` n `6`; index avg `-0.2174` n `25`; metal avg `-0.0619` n `20`; unknown avg `0.289` n `773`
- 24h: commodity avg `-0.4455` n `12`; crypto_alt avg `0.8093` n `230`; crypto_major avg `1.5331` n `8`; equity avg `0.3675` n `102`; fx avg `0.0857` n `6`; index avg `-0.0447` n `25`; metal avg `0.3019` n `20`; unknown avg `-0.0274` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
