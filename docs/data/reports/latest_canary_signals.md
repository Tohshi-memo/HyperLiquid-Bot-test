# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T18:22:40.793800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.1165` n `238`; crypto_major avg `0.0653` n `8`; equity avg `-0.0428` n `156`; fx avg `-0.0062` n `6`; index avg `0.0009` n `27`; metal avg `-0.0048` n `20`; unknown avg `0.534` n `1238`
- 1h: commodity avg `0.1337` n `13`; crypto_alt avg `-0.8691` n `238`; crypto_major avg `-0.4347` n `8`; equity avg `-0.4115` n `156`; fx avg `-0.0128` n `6`; index avg `-0.0343` n `27`; metal avg `-0.0964` n `20`; unknown avg `4.6165` n `1232`
- 4h: commodity avg `0.1473` n `13`; crypto_alt avg `0.4314` n `238`; crypto_major avg `0.7086` n `8`; equity avg `-0.7459` n `156`; fx avg `0.0642` n `6`; index avg `-0.0665` n `27`; metal avg `-0.0848` n `20`; unknown avg `34.4793` n `1174`
- 24h: commodity avg `-0.5502` n `13`; crypto_alt avg `0.3137` n `238`; crypto_major avg `1.9856` n `8`; equity avg `-1.0935` n `155`; fx avg `0.0321` n `6`; index avg `-0.1292` n `27`; metal avg `-0.453` n `20`; unknown avg `52.4882` n `946`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
