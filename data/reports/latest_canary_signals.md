# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T08:22:28.724170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1487` n `13`; crypto_alt avg `0.0825` n `239`; crypto_major avg `0.1273` n `8`; equity avg `0.0937` n `158`; fx avg `-0.0074` n `6`; index avg `0.0255` n `27`; metal avg `0.1347` n `20`; unknown avg `0.0975` n `1246`
- 1h: commodity avg `-0.1845` n `13`; crypto_alt avg `0.511` n `239`; crypto_major avg `0.4615` n `8`; equity avg `0.5006` n `158`; fx avg `-0.0168` n `6`; index avg `0.0816` n `27`; metal avg `0.2452` n `20`; unknown avg `0.6797` n `1194`
- 4h: commodity avg `-0.2219` n `13`; crypto_alt avg `0.5262` n `239`; crypto_major avg `0.0905` n `8`; equity avg `0.3716` n `158`; fx avg `-0.0907` n `6`; index avg `0.0292` n `27`; metal avg `0.2622` n `20`; unknown avg `0.2164` n `1166`
- 24h: commodity avg `0.9929` n `13`; crypto_alt avg `-3.9687` n `239`; crypto_major avg `-5.9217` n `8`; equity avg `-5.8883` n `158`; fx avg `-0.0316` n `6`; index avg `-0.7997` n `27`; metal avg `-0.2352` n `20`; unknown avg `241.017` n `991`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
