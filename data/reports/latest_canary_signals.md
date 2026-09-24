# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T13:37:30.773576+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0838` n `12`; crypto_alt avg `0.3133` n `234`; crypto_major avg `0.4031` n `8`; equity avg `0.3314` n `141`; fx avg `0.0039` n `6`; index avg `0.0199` n `26`; metal avg `-0.0628` n `20`; unknown avg `30.6729` n `943`
- 1h: commodity avg `0.0618` n `12`; crypto_alt avg `1.6128` n `234`; crypto_major avg `1.2576` n `8`; equity avg `0.6574` n `141`; fx avg `-0.0163` n `6`; index avg `0.0747` n `26`; metal avg `-0.0063` n `20`; unknown avg `31.5693` n `941`
- 4h: commodity avg `-0.0463` n `12`; crypto_alt avg `1.8563` n `234`; crypto_major avg `1.3176` n `8`; equity avg `0.7123` n `141`; fx avg `-0.0429` n `6`; index avg `0.0975` n `26`; metal avg `0.0372` n `20`; unknown avg `8.8547` n `935`
- 24h: commodity avg `0.6062` n `12`; crypto_alt avg `-2.5206` n `234`; crypto_major avg `-2.3721` n `8`; equity avg `-1.4642` n `141`; fx avg `0.0007` n `6`; index avg `-0.3208` n `26`; metal avg `-0.2657` n `20`; unknown avg `586.5468` n `819`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
