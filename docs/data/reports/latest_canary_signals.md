# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T01:07:25.050888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `13`; crypto_alt avg `0.209` n `239`; crypto_major avg `0.3849` n `8`; equity avg `0.6604` n `166`; fx avg `0.0366` n `6`; index avg `0.0942` n `27`; metal avg `-0.0761` n `20`; unknown avg `0.2011` n `1258`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `0.2408` n `239`; crypto_major avg `0.5832` n `8`; equity avg `0.9367` n `166`; fx avg `0.1115` n `6`; index avg `0.1707` n `27`; metal avg `0.1259` n `20`; unknown avg `0.3878` n `1262`
- 4h: commodity avg `0.112` n `13`; crypto_alt avg `-0.097` n `239`; crypto_major avg `-0.1089` n `8`; equity avg `0.8725` n `166`; fx avg `0.0885` n `6`; index avg `0.1581` n `27`; metal avg `0.1083` n `20`; unknown avg `204.1427` n `1236`
- 24h: commodity avg `-1.0492` n `13`; crypto_alt avg `1.4447` n `239`; crypto_major avg `1.6337` n `8`; equity avg `6.7234` n `166`; fx avg `-0.1396` n `6`; index avg `0.6801` n `27`; metal avg `0.4737` n `20`; unknown avg `357.8409` n `1051`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
