# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T10:52:30.242989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0285` n `13`; crypto_alt avg `-0.3292` n `237`; crypto_major avg `-0.1533` n `8`; equity avg `-0.0544` n `152`; fx avg `0.0013` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0111` n `20`; unknown avg `0.1702` n `1230`
- 1h: commodity avg `-0.0177` n `13`; crypto_alt avg `0.0514` n `237`; crypto_major avg `0.1335` n `8`; equity avg `0.0638` n `152`; fx avg `0.0071` n `6`; index avg `0.0008` n `26`; metal avg `-0.0066` n `20`; unknown avg `0.2661` n `1228`
- 4h: commodity avg `0.0364` n `13`; crypto_alt avg `-0.6635` n `237`; crypto_major avg `-0.699` n `8`; equity avg `-0.2048` n `152`; fx avg `0.0024` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0386` n `20`; unknown avg `12.0005` n `1194`
- 24h: commodity avg `0.1482` n `13`; crypto_alt avg `-2.6217` n `237`; crypto_major avg `-2.1167` n `8`; equity avg `-0.5259` n `152`; fx avg `-0.001` n `6`; index avg `0.0201` n `26`; metal avg `-0.1679` n `20`; unknown avg `193.6915` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
