# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T06:52:26.032118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `-0.0719` n `239`; crypto_major avg `-0.0294` n `8`; equity avg `0.0465` n `158`; fx avg `0.0` n `6`; index avg `0.0061` n `27`; metal avg `-0.0072` n `20`; unknown avg `0.0185` n `1260`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.1495` n `239`; crypto_major avg `-0.0367` n `8`; equity avg `0.0259` n `158`; fx avg `-0.001` n `6`; index avg `0.0045` n `27`; metal avg `-0.0031` n `20`; unknown avg `-0.0748` n `1224`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `0.0112` n `239`; crypto_major avg `0.2269` n `8`; equity avg `0.1314` n `158`; fx avg `0.0207` n `6`; index avg `-0.0` n `27`; metal avg `-0.003` n `20`; unknown avg `-0.1409` n `1208`
- 24h: commodity avg `0.155` n `13`; crypto_alt avg `-1.8797` n `239`; crypto_major avg `-0.721` n `8`; equity avg `0.0805` n `158`; fx avg `0.0506` n `6`; index avg `0.0347` n `27`; metal avg `-0.0498` n `20`; unknown avg `158.9029` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
