# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T08:37:22.910435+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1447` n `12`; crypto_alt avg `-0.156` n `228`; crypto_major avg `0.0256` n `8`; equity avg `0.0188` n `67`; fx avg `0.0065` n `6`; index avg `0.0295` n `23`; metal avg `-0.1389` n `18`; unknown avg `0.0144` n `417`
- 1h: commodity avg `0.1449` n `12`; crypto_alt avg `0.3746` n `228`; crypto_major avg `0.1859` n `8`; equity avg `0.2176` n `67`; fx avg `0.0162` n `6`; index avg `0.0804` n `23`; metal avg `-0.0352` n `18`; unknown avg `-0.075` n `417`
- 4h: commodity avg `0.7299` n `12`; crypto_alt avg `-0.0103` n `228`; crypto_major avg `-0.0526` n `8`; equity avg `-0.1055` n `67`; fx avg `-0.0` n `6`; index avg `-0.0226` n `23`; metal avg `-0.2161` n `18`; unknown avg `0.373` n `397`
- 24h: commodity avg `0.8001` n `12`; crypto_alt avg `-0.7914` n `228`; crypto_major avg `-1.6236` n `8`; equity avg `-0.5964` n `67`; fx avg `-0.0935` n `6`; index avg `-0.0774` n `23`; metal avg `-0.6724` n `18`; unknown avg `0.0812` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1791`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
