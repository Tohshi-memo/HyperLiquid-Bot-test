# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T23:07:11.642813+00:00`
- Correlation status: `ready`
- Asset price records: `592`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0417` n `12`; crypto_alt avg `0.2149` n `228`; crypto_major avg `0.1598` n `8`; equity avg `0.2678` n `65`; fx avg `-0.0038` n `5`; index avg `0.1183` n `23`; metal avg `0.1185` n `18`; unknown avg `0.0542` n `365`
- 1h: commodity avg `-0.1097` n `12`; crypto_alt avg `0.4867` n `228`; crypto_major avg `0.2788` n `8`; equity avg `0.2966` n `65`; fx avg `-0.0081` n `5`; index avg `0.115` n `23`; metal avg `0.1377` n `18`; unknown avg `0.0173` n `365`
- 4h: commodity avg `0.4797` n `12`; crypto_alt avg `0.2305` n `228`; crypto_major avg `-0.1182` n `8`; equity avg `-0.1327` n `65`; fx avg `-0.0358` n `5`; index avg `0.053` n `23`; metal avg `-0.4998` n `18`; unknown avg `-0.4872` n `365`
- 24h: commodity avg `0.8507` n `12`; crypto_alt avg `1.773` n `228`; crypto_major avg `-1.5801` n `8`; equity avg `-1.4262` n `65`; fx avg `0.15` n `5`; index avg `-0.8074` n `23`; metal avg `-0.3848` n `18`; unknown avg `-0.385` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1395`, n `588`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `588`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1107`, n `588`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `588`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `584`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `584`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.087`, n `584`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.087`, n `584`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0824`, n `584`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `584`, weak_sample_signal
