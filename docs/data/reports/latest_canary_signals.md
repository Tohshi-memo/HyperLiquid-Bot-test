# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T12:07:22.883403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `0.0485` n `239`; crypto_major avg `0.0433` n `8`; equity avg `-0.0343` n `158`; fx avg `0.0006` n `6`; index avg `-0.0018` n `27`; metal avg `0.0037` n `20`; unknown avg `-0.0716` n `1252`
- 1h: commodity avg `0.0384` n `13`; crypto_alt avg `0.2891` n `239`; crypto_major avg `0.3491` n `8`; equity avg `0.0613` n `158`; fx avg `-0.0009` n `6`; index avg `-0.0026` n `27`; metal avg `0.0141` n `20`; unknown avg `-0.1188` n `1250`
- 4h: commodity avg `0.0035` n `13`; crypto_alt avg `0.0777` n `239`; crypto_major avg `0.1598` n `8`; equity avg `0.1382` n `158`; fx avg `-0.0008` n `6`; index avg `-0.02` n `27`; metal avg `0.0038` n `20`; unknown avg `218.8593` n `1170`
- 24h: commodity avg `0.0711` n `13`; crypto_alt avg `-1.0238` n `239`; crypto_major avg `-0.2069` n `8`; equity avg `0.2289` n `158`; fx avg `0.0593` n `6`; index avg `0.0354` n `27`; metal avg `-0.0243` n `20`; unknown avg `5.5473` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
