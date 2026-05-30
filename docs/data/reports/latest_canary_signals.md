# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T01:52:16.356918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `-0.0531` n `228`; crypto_major avg `0.0033` n `8`; equity avg `0.0015` n `69`; fx avg `0.0006` n `6`; index avg `-0.0399` n `23`; metal avg `-0.0087` n `18`; unknown avg `0.0782` n `419`
- 1h: commodity avg `0.0547` n `12`; crypto_alt avg `0.6526` n `228`; crypto_major avg `0.5749` n `8`; equity avg `0.1162` n `69`; fx avg `0.0042` n `6`; index avg `-0.0751` n `23`; metal avg `-0.004` n `18`; unknown avg `-0.1038` n `419`
- 4h: commodity avg `0.3563` n `12`; crypto_alt avg `1.335` n `228`; crypto_major avg `1.0677` n `8`; equity avg `0.2926` n `69`; fx avg `0.0005` n `6`; index avg `-0.0253` n `23`; metal avg `0.0858` n `18`; unknown avg `-0.2914` n `419`
- 24h: commodity avg `-0.1367` n `12`; crypto_alt avg `1.5612` n `228`; crypto_major avg `1.8632` n `8`; equity avg `1.2407` n `69`; fx avg `0.1015` n `6`; index avg `0.19` n `23`; metal avg `-0.1082` n `18`; unknown avg `0.4584` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
