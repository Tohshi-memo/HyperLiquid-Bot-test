# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T18:22:24.245123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1315` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0225` n `12`; crypto_alt avg `0.3538` n `228`; crypto_major avg `0.2453` n `8`; equity avg `0.0206` n `74`; fx avg `0.0454` n `6`; index avg `0.0194` n `23`; metal avg `-0.0137` n `18`; unknown avg `0.1466` n `515`
- 1h: commodity avg `0.0482` n `12`; crypto_alt avg `-0.1035` n `228`; crypto_major avg `-0.2212` n `8`; equity avg `-0.1229` n `74`; fx avg `0.1742` n `6`; index avg `-0.0584` n `23`; metal avg `0.0025` n `18`; unknown avg `1.0447` n `515`
- 4h: commodity avg `0.1361` n `12`; crypto_alt avg `-1.2805` n `228`; crypto_major avg `-1.2125` n `8`; equity avg `-0.2387` n `74`; fx avg `0.2329` n `6`; index avg `-0.081` n `23`; metal avg `0.0425` n `18`; unknown avg `-1.214` n `515`
- 24h: commodity avg `0.3772` n `12`; crypto_alt avg `-1.0182` n `228`; crypto_major avg `-0.6844` n `8`; equity avg `-1.1248` n `74`; fx avg `0.1844` n `6`; index avg `-0.6003` n `23`; metal avg `-0.6748` n `18`; unknown avg `0.8474` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
