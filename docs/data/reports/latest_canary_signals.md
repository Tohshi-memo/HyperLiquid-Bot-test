# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T01:37:27.900984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.0973` n `239`; crypto_major avg `0.016` n `8`; equity avg `-0.0051` n `158`; fx avg `0.0096` n `6`; index avg `0.0044` n `27`; metal avg `0.0039` n `20`; unknown avg `0.5453` n `1260`
- 1h: commodity avg `0.1` n `13`; crypto_alt avg `-0.3557` n `239`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0599` n `158`; fx avg `0.0066` n `6`; index avg `-0.0062` n `27`; metal avg `0.0041` n `20`; unknown avg `0.3227` n `1254`
- 4h: commodity avg `-0.0276` n `13`; crypto_alt avg `0.2074` n `239`; crypto_major avg `0.3803` n `8`; equity avg `0.1055` n `158`; fx avg `0.0167` n `6`; index avg `0.0137` n `27`; metal avg `0.0087` n `20`; unknown avg `0.4617` n `1226`
- 24h: commodity avg `0.0396` n `13`; crypto_alt avg `-1.9067` n `239`; crypto_major avg `-0.872` n `8`; equity avg `-0.0649` n `158`; fx avg `0.0051` n `6`; index avg `0.0476` n `27`; metal avg `-0.0392` n `20`; unknown avg `161.5563` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
