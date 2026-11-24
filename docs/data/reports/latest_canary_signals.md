# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T01:37:26.431353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `-0.032` n `239`; crypto_major avg `-0.0615` n `8`; equity avg `-0.4114` n `166`; fx avg `-0.0046` n `6`; index avg `-0.031` n `27`; metal avg `0.0653` n `20`; unknown avg `0.0001` n `1266`
- 1h: commodity avg `-0.0964` n `13`; crypto_alt avg `0.6164` n `239`; crypto_major avg `0.812` n `8`; equity avg `0.5732` n `166`; fx avg `0.0502` n `6`; index avg `0.1126` n `27`; metal avg `0.102` n `20`; unknown avg `287.6364` n `1266`
- 4h: commodity avg `-0.0279` n `13`; crypto_alt avg `0.4194` n `239`; crypto_major avg `0.3219` n `8`; equity avg `0.595` n `166`; fx avg `0.0831` n `6`; index avg `0.1624` n `27`; metal avg `0.2748` n `20`; unknown avg `160.0459` n `1246`
- 24h: commodity avg `-1.1794` n `13`; crypto_alt avg `1.8212` n `239`; crypto_major avg `1.9234` n `8`; equity avg `6.0853` n `166`; fx avg `-0.1729` n `6`; index avg `0.6342` n `27`; metal avg `0.583` n `20`; unknown avg `329.8203` n `1049`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
