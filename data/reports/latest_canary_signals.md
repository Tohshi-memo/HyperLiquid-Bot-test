# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T05:37:14.251795+00:00`
- Correlation status: `ready`
- Asset price records: `618`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1206` n `12`; crypto_alt avg `0.0524` n `228`; crypto_major avg `0.1225` n `8`; equity avg `0.1205` n `65`; fx avg `0.0109` n `5`; index avg `0.0408` n `23`; metal avg `0.2986` n `18`; unknown avg `-0.6329` n `365`
- 1h: commodity avg `-0.285` n `12`; crypto_alt avg `0.0785` n `228`; crypto_major avg `0.2161` n `8`; equity avg `0.3239` n `65`; fx avg `-0.0016` n `5`; index avg `0.1031` n `23`; metal avg `0.5652` n `18`; unknown avg `-0.6911` n `365`
- 4h: commodity avg `-0.2373` n `12`; crypto_alt avg `0.3773` n `228`; crypto_major avg `0.0209` n `8`; equity avg `0.3494` n `65`; fx avg `0.0503` n `5`; index avg `0.0856` n `23`; metal avg `0.5266` n `18`; unknown avg `-0.9114` n `365`
- 24h: commodity avg `0.3674` n `12`; crypto_alt avg `1.17` n `228`; crypto_major avg `-1.5773` n `8`; equity avg `-0.8802` n `65`; fx avg `0.2463` n `5`; index avg `-0.5913` n `23`; metal avg `0.6894` n `18`; unknown avg `-0.2332` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `614`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1207`, n `610`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1203`, n `610`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `614`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `614`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `614`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `610`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.084`, n `610`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0797`, n `610`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `614`, weak_sample_signal
