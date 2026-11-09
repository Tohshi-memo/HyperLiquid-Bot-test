# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T21:52:35.530411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0766` n `13`; crypto_alt avg `0.055` n `239`; crypto_major avg `0.1258` n `8`; equity avg `0.0936` n `160`; fx avg `0.0009` n `6`; index avg `0.0162` n `27`; metal avg `0.0237` n `20`; unknown avg `-0.0164` n `1261`
- 1h: commodity avg `-0.1161` n `13`; crypto_alt avg `-0.1419` n `239`; crypto_major avg `-0.0848` n `8`; equity avg `0.2176` n `160`; fx avg `0.009` n `6`; index avg `0.0162` n `27`; metal avg `0.0268` n `20`; unknown avg `2.3346` n `1221`
- 4h: commodity avg `-0.2539` n `13`; crypto_alt avg `-0.0342` n `239`; crypto_major avg `0.1852` n `8`; equity avg `0.4158` n `160`; fx avg `-0.0042` n `6`; index avg `0.0897` n `27`; metal avg `0.3445` n `20`; unknown avg `2.3472` n `1211`
- 24h: commodity avg `-0.3723` n `13`; crypto_alt avg `1.6605` n `239`; crypto_major avg `-0.953` n `8`; equity avg `4.8849` n `160`; fx avg `-0.106` n `6`; index avg `0.6358` n `27`; metal avg `0.7216` n `20`; unknown avg `4.5477` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
