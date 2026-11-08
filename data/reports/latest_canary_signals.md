# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T11:07:28.477103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.0188` n `239`; crypto_major avg `-0.029` n `8`; equity avg `-0.0198` n `158`; fx avg `0.0022` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0116` n `20`; unknown avg `0.11` n `1258`
- 1h: commodity avg `-0.0316` n `13`; crypto_alt avg `-0.0954` n `239`; crypto_major avg `-0.0242` n `8`; equity avg `-0.072` n `158`; fx avg `0.0074` n `6`; index avg `0.0013` n `27`; metal avg `-0.0044` n `20`; unknown avg `0.1081` n `1256`
- 4h: commodity avg `-0.0047` n `13`; crypto_alt avg `-0.1778` n `239`; crypto_major avg `-0.0773` n `8`; equity avg `0.1347` n `158`; fx avg `0.005` n `6`; index avg `-0.0001` n `27`; metal avg `-0.0034` n `20`; unknown avg `221.082` n `1160`
- 24h: commodity avg `0.0444` n `13`; crypto_alt avg `-1.3898` n `239`; crypto_major avg `-0.6742` n `8`; equity avg `0.1232` n `158`; fx avg `0.0553` n `6`; index avg `0.0246` n `27`; metal avg `-0.0522` n `20`; unknown avg `5.7131` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
