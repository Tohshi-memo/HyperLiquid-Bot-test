# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T22:37:19.655665+00:00`
- Correlation status: `ready`
- Asset price records: `590`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.11` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.2202` n `12`; crypto_alt avg `-0.3139` n `228`; crypto_major avg `-0.2208` n `8`; equity avg `-0.1905` n `65`; fx avg `-0.0067` n `5`; index avg `-0.1031` n `23`; metal avg `-0.1474` n `18`; unknown avg `-0.0418` n `365`
- 1h: commodity avg `-0.3636` n `12`; crypto_alt avg `-0.2334` n `228`; crypto_major avg `-0.3108` n `8`; equity avg `-0.2408` n `65`; fx avg `-0.0004` n `5`; index avg `0.0503` n `23`; metal avg `0.0566` n `18`; unknown avg `0.299` n `365`
- 4h: commodity avg `0.6844` n `12`; crypto_alt avg `-0.6237` n `228`; crypto_major avg `-0.6892` n `8`; equity avg `-0.7044` n `65`; fx avg `-0.0264` n `5`; index avg `-0.0702` n `23`; metal avg `-0.6607` n `18`; unknown avg `-0.6812` n `365`
- 24h: commodity avg `0.7712` n `12`; crypto_alt avg `1.0257` n `228`; crypto_major avg `-2.0565` n `8`; equity avg `-1.679` n `65`; fx avg `0.1639` n `5`; index avg `-0.8409` n `23`; metal avg `-0.3688` n `18`; unknown avg `-0.5661` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `586`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `586`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `586`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `586`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `582`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `582`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.091`, n `582`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0881`, n `582`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0828`, n `582`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `582`, weak_sample_signal
