# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T15:07:27.998273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `0.1332` n `228`; crypto_major avg `0.0992` n `8`; equity avg `-0.0161` n `88`; fx avg `-0.0128` n `6`; index avg `-0.002` n `23`; metal avg `0.0022` n `20`; unknown avg `0.0214` n `764`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `0.6586` n `228`; crypto_major avg `0.1299` n `8`; equity avg `0.0313` n `88`; fx avg `0.0037` n `6`; index avg `0.0213` n `23`; metal avg `-0.0303` n `20`; unknown avg `2.6243` n `764`
- 4h: commodity avg `0.1179` n `12`; crypto_alt avg `0.6728` n `228`; crypto_major avg `0.1659` n `8`; equity avg `0.0514` n `88`; fx avg `-0.0075` n `6`; index avg `0.0268` n `23`; metal avg `-0.0409` n `20`; unknown avg `2.5449` n `764`
- 24h: commodity avg `0.2044` n `12`; crypto_alt avg `-0.1452` n `228`; crypto_major avg `-1.399` n `8`; equity avg `-0.0019` n `88`; fx avg `-0.0137` n `6`; index avg `-0.0503` n `23`; metal avg `-0.0584` n `20`; unknown avg `16.3223` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
