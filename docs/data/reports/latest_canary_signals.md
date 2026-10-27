# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T17:22:33.218254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `0.0271` n `238`; crypto_major avg `0.0493` n `8`; equity avg `0.0413` n `154`; fx avg `0.0002` n `6`; index avg `0.0009` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.1735` n `1236`
- 1h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.0363` n `238`; crypto_major avg `0.2614` n `8`; equity avg `-0.045` n `154`; fx avg `0.009` n `6`; index avg `-0.0846` n `27`; metal avg `0.0345` n `20`; unknown avg `0.8989` n `1234`
- 4h: commodity avg `-0.18` n `13`; crypto_alt avg `0.8933` n `238`; crypto_major avg `0.8757` n `8`; equity avg `1.5631` n `154`; fx avg `-0.033` n `6`; index avg `0.1814` n `27`; metal avg `0.3071` n `20`; unknown avg `0.5051` n `1150`
- 24h: commodity avg `-0.5375` n `13`; crypto_alt avg `0.1423` n `237`; crypto_major avg `0.7913` n `8`; equity avg `1.2389` n `154`; fx avg `-0.068` n `6`; index avg `0.3269` n `27`; metal avg `0.0599` n `20`; unknown avg `25.3` n `1044`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2014`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
