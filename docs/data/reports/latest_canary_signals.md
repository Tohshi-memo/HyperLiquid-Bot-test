# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T05:37:26.848096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.0562` n `239`; crypto_major avg `0.1287` n `8`; equity avg `0.1317` n `164`; fx avg `-0.0058` n `6`; index avg `0.0211` n `27`; metal avg `0.1107` n `20`; unknown avg `-0.0936` n `1266`
- 1h: commodity avg `-0.0025` n `13`; crypto_alt avg `-0.3979` n `239`; crypto_major avg `0.049` n `8`; equity avg `-0.0445` n `164`; fx avg `-0.0139` n `6`; index avg `0.0016` n `27`; metal avg `0.1491` n `20`; unknown avg `0.555` n `1262`
- 4h: commodity avg `-0.0303` n `13`; crypto_alt avg `0.972` n `239`; crypto_major avg `1.4907` n `8`; equity avg `0.7609` n `164`; fx avg `-0.0037` n `6`; index avg `0.1332` n `27`; metal avg `0.0643` n `20`; unknown avg `3.398` n `1239`
- 24h: commodity avg `0.1294` n `13`; crypto_alt avg `-0.0815` n `239`; crypto_major avg `-1.0719` n `8`; equity avg `-0.4447` n `164`; fx avg `-0.1078` n `6`; index avg `0.0732` n `27`; metal avg `-0.4525` n `20`; unknown avg `202.7195` n `1115`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
