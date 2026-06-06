# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T12:37:30.567351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.9638` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.874` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0739` n `228`; crypto_major avg `-0.1795` n `8`; equity avg `0.0149` n `74`; fx avg `-0.0004` n `6`; index avg `0.1386` n `23`; metal avg `-0.0036` n `18`; unknown avg `0.0723` n `425`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0937` n `228`; crypto_major avg `-0.1314` n `8`; equity avg `0.3109` n `74`; fx avg `-0.001` n `6`; index avg `0.3581` n `23`; metal avg `0.0378` n `18`; unknown avg `0.1286` n `421`
- 4h: commodity avg `0.137` n `12`; crypto_alt avg `-1.0751` n `228`; crypto_major avg `-1.3279` n `8`; equity avg `0.6359` n `74`; fx avg `0.0082` n `6`; index avg `0.5461` n `23`; metal avg `-0.01` n `18`; unknown avg `0.1585` n `421`
- 24h: commodity avg `-1.1288` n `12`; crypto_alt avg `-3.0959` n `228`; crypto_major avg `-3.206` n `8`; equity avg `-5.8717` n `74`; fx avg `-0.2376` n `6`; index avg `-3.513` n `23`; metal avg `-4.1628` n `18`; unknown avg `-0.6389` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
