# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T00:37:31.143008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2381` n `12`; crypto_alt avg `0.1538` n `228`; crypto_major avg `0.2061` n `8`; equity avg `0.232` n `74`; fx avg `-0.0395` n `6`; index avg `-0.0081` n `23`; metal avg `0.0957` n `18`; unknown avg `0.013` n `556`
- 1h: commodity avg `0.3679` n `12`; crypto_alt avg `0.4897` n `228`; crypto_major avg `0.1392` n `8`; equity avg `0.5554` n `74`; fx avg `-0.0023` n `6`; index avg `0.0405` n `23`; metal avg `0.0975` n `18`; unknown avg `0.1149` n `556`
- 4h: commodity avg `0.0439` n `12`; crypto_alt avg `0.7355` n `228`; crypto_major avg `0.7177` n `8`; equity avg `1.1308` n `74`; fx avg `0.0157` n `6`; index avg `0.3052` n `23`; metal avg `0.2632` n `18`; unknown avg `-0.1668` n `556`
- 24h: commodity avg `-2.5491` n `12`; crypto_alt avg `4.0965` n `228`; crypto_major avg `4.1522` n `8`; equity avg `5.1801` n `74`; fx avg `0.0291` n `6`; index avg `2.7305` n `23`; metal avg `4.0205` n `18`; unknown avg `2.7805` n `530`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
