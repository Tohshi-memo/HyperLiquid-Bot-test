# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T13:07:31.044037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0136` n `13`; crypto_alt avg `0.1684` n `239`; crypto_major avg `0.1007` n `8`; equity avg `-0.0409` n `164`; fx avg `-0.002` n `6`; index avg `-0.0034` n `27`; metal avg `0.0099` n `20`; unknown avg `0.1028` n `1260`
- 1h: commodity avg `0.0613` n `13`; crypto_alt avg `0.171` n `239`; crypto_major avg `0.2654` n `8`; equity avg `-0.0588` n `164`; fx avg `-0.0011` n `6`; index avg `-0.0177` n `27`; metal avg `0.0125` n `20`; unknown avg `0.1292` n `1262`
- 4h: commodity avg `0.1155` n `13`; crypto_alt avg `0.1273` n `239`; crypto_major avg `0.249` n `8`; equity avg `0.3308` n `164`; fx avg `-0.0189` n `6`; index avg `0.0782` n `27`; metal avg `-0.1447` n `20`; unknown avg `0.9442` n `1254`
- 24h: commodity avg `-0.1594` n `13`; crypto_alt avg `0.7094` n `239`; crypto_major avg `0.5379` n `8`; equity avg `1.5065` n `164`; fx avg `0.0098` n `6`; index avg `0.3587` n `27`; metal avg `-0.1773` n `20`; unknown avg `2.6227` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
