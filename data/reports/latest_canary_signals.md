# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T22:37:29.413011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `0.2273` n `239`; crypto_major avg `0.2035` n `8`; equity avg `-0.0241` n `158`; fx avg `0.0039` n `6`; index avg `0.0452` n `27`; metal avg `0.0094` n `20`; unknown avg `18.6208` n `1264`
- 1h: commodity avg `-0.0621` n `13`; crypto_alt avg `0.8987` n `239`; crypto_major avg `0.7283` n `8`; equity avg `0.038` n `158`; fx avg `-0.0014` n `6`; index avg `0.0245` n `27`; metal avg `0.0092` n `20`; unknown avg `-1.4219` n `1258`
- 4h: commodity avg `-0.1767` n `13`; crypto_alt avg `0.7071` n `239`; crypto_major avg `0.3072` n `8`; equity avg `0.2773` n `158`; fx avg `0.0204` n `6`; index avg `0.066` n `27`; metal avg `0.0267` n `20`; unknown avg `-0.8308` n `1194`
- 24h: commodity avg `-1.8947` n `13`; crypto_alt avg `2.3054` n `239`; crypto_major avg `2.465` n `8`; equity avg `-1.4103` n `158`; fx avg `0.0686` n `6`; index avg `0.1164` n `27`; metal avg `1.2355` n `20`; unknown avg `-0.6821` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2658`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
