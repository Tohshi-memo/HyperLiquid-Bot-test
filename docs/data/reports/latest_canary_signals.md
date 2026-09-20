# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T18:55:08.043317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `-0.3668` n `234`; crypto_major avg `-0.2412` n `8`; equity avg `-0.0161` n `140`; fx avg `-0.0048` n `6`; index avg `0.002` n `26`; metal avg `0.0005` n `20`; unknown avg `0.9709` n `943`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.4983` n `234`; crypto_major avg `-0.2211` n `8`; equity avg `-0.0634` n `140`; fx avg `0.0008` n `6`; index avg `0.0004` n `26`; metal avg `-0.0347` n `20`; unknown avg `33.6196` n `933`
- 4h: commodity avg `-0.0241` n `12`; crypto_alt avg `2.0807` n `234`; crypto_major avg `1.2366` n `8`; equity avg `0.2414` n `140`; fx avg `-0.0117` n `6`; index avg `0.0316` n `26`; metal avg `-0.0105` n `20`; unknown avg `1.6495` n `871`
- 24h: commodity avg `0.3634` n `12`; crypto_alt avg `-0.0865` n `234`; crypto_major avg `-0.8285` n `8`; equity avg `-0.12` n `140`; fx avg `-0.0304` n `6`; index avg `-0.0386` n `26`; metal avg `-0.0426` n `20`; unknown avg `62.6235` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
