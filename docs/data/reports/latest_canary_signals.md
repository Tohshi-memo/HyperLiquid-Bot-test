# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T23:37:22.501545+00:00`
- Correlation status: `ready`
- Asset price records: `594`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0959` n `12`; crypto_alt avg `0.1628` n `228`; crypto_major avg `0.0529` n `8`; equity avg `0.0302` n `65`; fx avg `-0.008` n `5`; index avg `-0.0448` n `23`; metal avg `0.027` n `18`; unknown avg `-0.2539` n `365`
- 1h: commodity avg `-0.0227` n `12`; crypto_alt avg `0.5259` n `228`; crypto_major avg `0.2377` n `8`; equity avg `0.4998` n `65`; fx avg `-0.0189` n `5`; index avg `0.097` n `23`; metal avg `0.237` n `18`; unknown avg `-0.19` n `365`
- 4h: commodity avg `0.4727` n `12`; crypto_alt avg `0.145` n `228`; crypto_major avg `-0.1864` n `8`; equity avg `-0.0638` n `65`; fx avg `-0.0452` n `5`; index avg `-0.0338` n `23`; metal avg `-0.2952` n `18`; unknown avg `-0.3013` n `365`
- 24h: commodity avg `0.8211` n `12`; crypto_alt avg `1.5099` n `228`; crypto_major avg `-1.7887` n `8`; equity avg `-1.4716` n `65`; fx avg `0.1334` n `5`; index avg `-0.8419` n `23`; metal avg `-0.0868` n `18`; unknown avg `-0.5796` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.139`, n `590`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `590`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `590`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `590`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `586`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `586`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `586`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0844`, n `586`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0795`, n `586`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0753`, n `586`, weak_sample_signal
