# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T13:52:31.630838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0949` n `13`; crypto_alt avg `-0.0186` n `239`; crypto_major avg `0.1099` n `8`; equity avg `0.3659` n `158`; fx avg `-0.0157` n `6`; index avg `0.0493` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.2899` n `1257`
- 1h: commodity avg `0.0986` n `13`; crypto_alt avg `0.0467` n `239`; crypto_major avg `0.0329` n `8`; equity avg `0.0809` n `158`; fx avg `-0.0508` n `6`; index avg `0.0566` n `27`; metal avg `-0.094` n `20`; unknown avg `52.6404` n `1253`
- 4h: commodity avg `0.3104` n `13`; crypto_alt avg `0.4438` n `239`; crypto_major avg `0.0508` n `8`; equity avg `0.2951` n `158`; fx avg `0.0337` n `6`; index avg `0.0306` n `27`; metal avg `-0.1114` n `20`; unknown avg `50.9403` n `1176`
- 24h: commodity avg `0.6367` n `13`; crypto_alt avg `-2.2953` n `239`; crypto_major avg `-4.4979` n `8`; equity avg `-3.3686` n `158`; fx avg `-0.0288` n `6`; index avg `-0.5169` n `27`; metal avg `-0.6223` n `20`; unknown avg `88.7155` n `1078`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
