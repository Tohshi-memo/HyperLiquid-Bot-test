# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T07:07:25.826372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `13`; crypto_alt avg `-0.239` n `238`; crypto_major avg `-0.1784` n `8`; equity avg `-0.0082` n `156`; fx avg `0.0065` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0127` n `20`; unknown avg `4.4269` n `1256`
- 1h: commodity avg `-0.0223` n `13`; crypto_alt avg `0.0412` n `238`; crypto_major avg `-0.1086` n `8`; equity avg `0.011` n `156`; fx avg `0.004` n `6`; index avg `-0.0065` n `27`; metal avg `0.0059` n `20`; unknown avg `4.496` n `1250`
- 4h: commodity avg `0.0124` n `13`; crypto_alt avg `-0.6279` n `238`; crypto_major avg `-0.4862` n `8`; equity avg `-0.0202` n `156`; fx avg `0.0105` n `6`; index avg `-0.0401` n `27`; metal avg `0.0203` n `20`; unknown avg `-0.1392` n `1214`
- 24h: commodity avg `0.0114` n `13`; crypto_alt avg `0.591` n `238`; crypto_major avg `-1.7979` n `8`; equity avg `-2.4091` n `156`; fx avg `-0.0721` n `6`; index avg `-0.2245` n `27`; metal avg `-0.4664` n `20`; unknown avg `4.1855` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
