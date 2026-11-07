# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T17:52:26.848326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `0.0633` n `239`; crypto_major avg `-0.0193` n `8`; equity avg `0.014` n `158`; fx avg `-0.0103` n `6`; index avg `0.0179` n `27`; metal avg `-0.0042` n `20`; unknown avg `1.155` n `1258`
- 1h: commodity avg `0.0062` n `13`; crypto_alt avg `0.3391` n `239`; crypto_major avg `0.1715` n `8`; equity avg `0.1404` n `158`; fx avg `-0.0107` n `6`; index avg `0.0355` n `27`; metal avg `0.0022` n `20`; unknown avg `0.64` n `1239`
- 4h: commodity avg `0.0517` n `13`; crypto_alt avg `-0.1507` n `239`; crypto_major avg `-0.2061` n `8`; equity avg `-0.0683` n `158`; fx avg `-0.0285` n `6`; index avg `0.032` n `27`; metal avg `-0.025` n `20`; unknown avg `163.1344` n `1225`
- 24h: commodity avg `0.2649` n `13`; crypto_alt avg `-1.0826` n `239`; crypto_major avg `-0.2746` n `8`; equity avg `1.2611` n `158`; fx avg `0.0158` n `6`; index avg `0.1409` n `27`; metal avg `0.0891` n `20`; unknown avg `0.1045` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
