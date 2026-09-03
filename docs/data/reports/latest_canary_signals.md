# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T09:52:27.467744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.1155` n `232`; crypto_major avg `-0.0566` n `8`; equity avg `-0.0471` n `133`; fx avg `-0.0144` n `6`; index avg `3.3274` n `26`; metal avg `-0.0289` n `20`; unknown avg `0.4355` n `792`
- 1h: commodity avg `0.1019` n `12`; crypto_alt avg `-0.123` n `232`; crypto_major avg `-0.2074` n `8`; equity avg `-0.2179` n `133`; fx avg `-0.0248` n `6`; index avg `-0.0468` n `26`; metal avg `-0.0709` n `20`; unknown avg `0.6666` n `790`
- 4h: commodity avg `0.2794` n `12`; crypto_alt avg `0.2065` n `232`; crypto_major avg `-0.0153` n `8`; equity avg `-0.1017` n `133`; fx avg `-0.1392` n `6`; index avg `-0.0566` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.0057` n `754`
- 24h: commodity avg `0.3558` n `12`; crypto_alt avg `1.4979` n `232`; crypto_major avg `1.4904` n `8`; equity avg `1.675` n `133`; fx avg `-0.4173` n `6`; index avg `0.1769` n `26`; metal avg `0.8653` n `20`; unknown avg `-0.0458` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.044`, n `668`, weak_sample_signal
