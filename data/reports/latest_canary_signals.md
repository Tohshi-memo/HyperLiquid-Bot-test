# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T19:22:26.700649+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0562` n `13`; crypto_alt avg `0.1812` n `239`; crypto_major avg `0.216` n `8`; equity avg `0.2635` n `164`; fx avg `0.0011` n `6`; index avg `0.0274` n `27`; metal avg `-0.0102` n `20`; unknown avg `0.368` n `1263`
- 1h: commodity avg `0.213` n `13`; crypto_alt avg `0.0162` n `239`; crypto_major avg `-0.1904` n `8`; equity avg `-0.098` n `164`; fx avg `0.0033` n `6`; index avg `-0.0113` n `27`; metal avg `-0.0336` n `20`; unknown avg `-0.0906` n `1263`
- 4h: commodity avg `0.0558` n `13`; crypto_alt avg `-0.4016` n `239`; crypto_major avg `-0.3881` n `8`; equity avg `-0.4907` n `164`; fx avg `0.0019` n `6`; index avg `-0.0443` n `27`; metal avg `-0.0911` n `20`; unknown avg `0.1657` n `1257`
- 24h: commodity avg `-0.2185` n `13`; crypto_alt avg `0.3914` n `239`; crypto_major avg `-0.3379` n `8`; equity avg `0.1891` n `164`; fx avg `-0.1735` n `6`; index avg `0.0385` n `27`; metal avg `-1.1856` n `20`; unknown avg `-0.1902` n `1138`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0528`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
