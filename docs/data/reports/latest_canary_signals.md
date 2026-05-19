# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T19:37:18.325984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0641` n `12`; crypto_alt avg `0.0451` n `228`; crypto_major avg `0.0952` n `8`; equity avg `-0.0788` n `66`; fx avg `0.0037` n `6`; index avg `-0.1919` n `23`; metal avg `-0.0046` n `18`; unknown avg `0.1726` n `383`
- 1h: commodity avg `-0.0158` n `12`; crypto_alt avg `-0.0903` n `228`; crypto_major avg `-0.0035` n `8`; equity avg `-0.4579` n `66`; fx avg `0.0012` n `6`; index avg `-0.3093` n `23`; metal avg `-0.1545` n `18`; unknown avg `0.1083` n `383`
- 4h: commodity avg `0.4902` n `12`; crypto_alt avg `0.2888` n `228`; crypto_major avg `0.1273` n `8`; equity avg `0.8214` n `66`; fx avg `-0.0327` n `6`; index avg `0.4695` n `23`; metal avg `-0.2042` n `18`; unknown avg `1.5116` n `383`
- 24h: commodity avg `1.2752` n `12`; crypto_alt avg `0.2125` n `228`; crypto_major avg `0.4898` n `8`; equity avg `0.6192` n `66`; fx avg `0.0662` n `6`; index avg `-0.2809` n `23`; metal avg `-2.298` n `18`; unknown avg `1.3042` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
