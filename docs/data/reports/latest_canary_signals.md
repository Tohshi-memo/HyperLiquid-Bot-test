# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T16:22:26.786970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0662` n `13`; crypto_alt avg `-0.0059` n `235`; crypto_major avg `0.0369` n `8`; equity avg `0.0108` n `144`; fx avg `-0.0012` n `6`; index avg `-0.0011` n `26`; metal avg `0.0039` n `20`; unknown avg `1.0967` n `1078`
- 1h: commodity avg `-0.0829` n `13`; crypto_alt avg `-0.2873` n `235`; crypto_major avg `-0.1297` n `8`; equity avg `-0.0243` n `144`; fx avg `0.0059` n `6`; index avg `-0.0091` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.7509` n `1070`
- 4h: commodity avg `-0.0994` n `13`; crypto_alt avg `0.0321` n `235`; crypto_major avg `-0.0315` n `8`; equity avg `0.0224` n `144`; fx avg `0.0073` n `6`; index avg `-0.0261` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.0116` n `1070`
- 24h: commodity avg `0.0132` n `13`; crypto_alt avg `0.897` n `235`; crypto_major avg `0.9976` n `8`; equity avg `0.2265` n `144`; fx avg `0.0173` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0135` n `20`; unknown avg `-0.0949` n `1019`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
