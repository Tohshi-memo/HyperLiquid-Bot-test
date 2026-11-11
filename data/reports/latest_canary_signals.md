# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T12:22:33.304817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0162` n `13`; crypto_alt avg `0.059` n `239`; crypto_major avg `0.1015` n `8`; equity avg `0.0782` n `161`; fx avg `0.0052` n `6`; index avg `0.0025` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.5471` n `1261`
- 1h: commodity avg `0.1263` n `13`; crypto_alt avg `0.0487` n `239`; crypto_major avg `-0.2073` n `8`; equity avg `0.1521` n `161`; fx avg `0.0032` n `6`; index avg `0.0051` n `27`; metal avg `-0.1159` n `20`; unknown avg `19.627` n `1249`
- 4h: commodity avg `0.3523` n `13`; crypto_alt avg `0.1714` n `239`; crypto_major avg `-0.03` n `8`; equity avg `0.6025` n `161`; fx avg `-0.0076` n `6`; index avg `0.0278` n `27`; metal avg `0.0079` n `20`; unknown avg `40.7274` n `1233`
- 24h: commodity avg `0.805` n `13`; crypto_alt avg `-0.6272` n `239`; crypto_major avg `-1.3274` n `8`; equity avg `3.1851` n `161`; fx avg `-0.2174` n `6`; index avg `0.285` n `27`; metal avg `0.1945` n `20`; unknown avg `1.4691` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
