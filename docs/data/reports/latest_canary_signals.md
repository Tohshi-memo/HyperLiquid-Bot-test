# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T17:37:27.320501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.4168` n `237`; crypto_major avg `-0.1665` n `8`; equity avg `-0.0943` n `152`; fx avg `-0.0087` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.607` n `1231`
- 1h: commodity avg `-0.0008` n `13`; crypto_alt avg `0.421` n `237`; crypto_major avg `0.5039` n `8`; equity avg `0.2214` n `152`; fx avg `-0.0081` n `6`; index avg `0.0336` n `26`; metal avg `0.0346` n `20`; unknown avg `1.0539` n `1207`
- 4h: commodity avg `0.0233` n `13`; crypto_alt avg `-1.2965` n `237`; crypto_major avg `-0.9211` n `8`; equity avg `-0.334` n `152`; fx avg `-0.0289` n `6`; index avg `-0.0474` n `26`; metal avg `-0.1057` n `20`; unknown avg `0.9679` n `1198`
- 24h: commodity avg `0.1632` n `13`; crypto_alt avg `-4.1988` n `237`; crypto_major avg `-2.9332` n `8`; equity avg `-0.8065` n `152`; fx avg `-0.0321` n `6`; index avg `-0.0655` n `26`; metal avg `-0.1802` n `20`; unknown avg `-0.5537` n `1045`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
