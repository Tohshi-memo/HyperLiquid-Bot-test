# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T15:07:36.817565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `-0.0681` n `8`; equity avg `-0.0301` n `113`; fx avg `-0.0007` n `6`; index avg `-0.0166` n `25`; metal avg `0.0427` n `20`; unknown avg `-0.0368` n `784`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.3064` n `230`; crypto_major avg `-0.1796` n `8`; equity avg `-0.3091` n `113`; fx avg `0.0036` n `6`; index avg `-0.0329` n `25`; metal avg `0.2232` n `20`; unknown avg `0.0879` n `784`
- 4h: commodity avg `0.396` n `12`; crypto_alt avg `-0.2434` n `230`; crypto_major avg `-0.4073` n `8`; equity avg `-0.4673` n `113`; fx avg `0.0399` n `6`; index avg `-0.0126` n `25`; metal avg `0.1718` n `20`; unknown avg `0.2621` n `784`
- 24h: commodity avg `1.0223` n `12`; crypto_alt avg `-0.0709` n `230`; crypto_major avg `-0.9509` n `8`; equity avg `-1.1018` n `113`; fx avg `0.2545` n `6`; index avg `-0.021` n `25`; metal avg `-0.05` n `20`; unknown avg `103.5322` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
