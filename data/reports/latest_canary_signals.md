# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T04:52:26.587636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `13`; crypto_alt avg `-0.0401` n `239`; crypto_major avg `-0.1269` n `8`; equity avg `-0.0093` n `158`; fx avg `0.0026` n `6`; index avg `-0.0036` n `27`; metal avg `-0.001` n `20`; unknown avg `0.3034` n `1257`
- 1h: commodity avg `-0.0001` n `13`; crypto_alt avg `0.2287` n `239`; crypto_major avg `-0.0918` n `8`; equity avg `0.0105` n `158`; fx avg `0.0017` n `6`; index avg `-0.0022` n `27`; metal avg `0.0076` n `20`; unknown avg `-0.3484` n `1239`
- 4h: commodity avg `-0.1181` n `13`; crypto_alt avg `-0.3914` n `239`; crypto_major avg `-0.3772` n `8`; equity avg `0.0489` n `158`; fx avg `0.0104` n `6`; index avg `0.015` n `27`; metal avg `0.011` n `20`; unknown avg `0.7746` n `1233`
- 24h: commodity avg `-0.263` n `13`; crypto_alt avg `0.2838` n `239`; crypto_major avg `-0.1557` n `8`; equity avg `1.1531` n `158`; fx avg `-0.0557` n `6`; index avg `0.1535` n `27`; metal avg `0.243` n `20`; unknown avg `8.4676` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
