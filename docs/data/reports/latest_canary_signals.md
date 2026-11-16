# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T07:22:26.223793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `13`; crypto_alt avg `-0.2207` n `239`; crypto_major avg `-0.2496` n `8`; equity avg `-0.1139` n `162`; fx avg `-0.001` n `6`; index avg `-0.0142` n `27`; metal avg `-0.0177` n `20`; unknown avg `79.2639` n `1261`
- 1h: commodity avg `-0.0303` n `13`; crypto_alt avg `-0.1209` n `239`; crypto_major avg `0.055` n `8`; equity avg `0.2316` n `162`; fx avg `0.0006` n `6`; index avg `0.0326` n `27`; metal avg `-0.0507` n `20`; unknown avg `88.0913` n `1137`
- 4h: commodity avg `0.2319` n `13`; crypto_alt avg `-1.1017` n `239`; crypto_major avg `-0.9235` n `8`; equity avg `-1.0882` n `162`; fx avg `-0.0448` n `6`; index avg `-0.1055` n `27`; metal avg `-0.0819` n `20`; unknown avg `89.6541` n `1115`
- 24h: commodity avg `-0.2288` n `13`; crypto_alt avg `-0.3359` n `239`; crypto_major avg `0.4582` n `8`; equity avg `-0.4537` n `162`; fx avg `-0.0588` n `6`; index avg `-0.0279` n `27`; metal avg `0.072` n `20`; unknown avg `0.8689` n `1077`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
