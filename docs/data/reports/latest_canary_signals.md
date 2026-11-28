# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T17:37:27.794885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `0.0449` n `239`; crypto_major avg `-0.1129` n `8`; equity avg `-0.004` n `168`; fx avg `-0.0013` n `6`; index avg `-0.0028` n `27`; metal avg `-0.0092` n `20`; unknown avg `9.621` n `1262`
- 1h: commodity avg `-0.0123` n `13`; crypto_alt avg `0.0193` n `239`; crypto_major avg `0.1183` n `8`; equity avg `0.0451` n `168`; fx avg `-0.0173` n `6`; index avg `-0.0059` n `27`; metal avg `0.0076` n `20`; unknown avg `57.9731` n `1231`
- 4h: commodity avg `-0.0458` n `13`; crypto_alt avg `-0.6385` n `239`; crypto_major avg `0.1693` n `8`; equity avg `0.006` n `168`; fx avg `0.0102` n `6`; index avg `-0.0052` n `27`; metal avg `0.0075` n `20`; unknown avg `45.5513` n `1219`
- 24h: commodity avg `-0.0903` n `13`; crypto_alt avg `-2.797` n `239`; crypto_major avg `-0.9762` n `8`; equity avg `0.3856` n `168`; fx avg `-0.0196` n `6`; index avg `0.0166` n `27`; metal avg `0.2363` n `20`; unknown avg `193.0862` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
