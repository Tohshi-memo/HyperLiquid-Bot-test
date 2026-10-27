# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T02:52:28.930714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `13`; crypto_alt avg `-0.0112` n `237`; crypto_major avg `0.0018` n `8`; equity avg `-0.0884` n `154`; fx avg `0.0171` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0696` n `20`; unknown avg `1.0325` n `1238`
- 1h: commodity avg `-0.0045` n `13`; crypto_alt avg `-0.3443` n `237`; crypto_major avg `-0.2482` n `8`; equity avg `-0.3367` n `154`; fx avg `0.0266` n `6`; index avg `-0.0413` n `27`; metal avg `-0.0178` n `20`; unknown avg `2.16` n `1236`
- 4h: commodity avg `-0.0726` n `13`; crypto_alt avg `-0.1856` n `237`; crypto_major avg `0.0881` n `8`; equity avg `0.0167` n `154`; fx avg `0.0161` n `6`; index avg `0.0747` n `27`; metal avg `-0.0944` n `20`; unknown avg `3.174` n `1220`
- 24h: commodity avg `0.027` n `13`; crypto_alt avg `0.6974` n `237`; crypto_major avg `1.1459` n `8`; equity avg `2.0887` n `153`; fx avg `0.0164` n `6`; index avg `0.1527` n `27`; metal avg `-0.0318` n `20`; unknown avg `997.9979` n `1004`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1906`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
