# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T03:37:25.268927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0086` n `13`; crypto_alt avg `0.1384` n `238`; crypto_major avg `0.2066` n `8`; equity avg `0.1315` n `154`; fx avg `-0.0032` n `6`; index avg `0.0127` n `27`; metal avg `-0.0189` n `20`; unknown avg `0.0982` n `1234`
- 1h: commodity avg `-0.0139` n `13`; crypto_alt avg `0.1327` n `238`; crypto_major avg `0.3006` n `8`; equity avg `0.5023` n `154`; fx avg `0.0` n `6`; index avg `0.0478` n `27`; metal avg `-0.0236` n `20`; unknown avg `320.1426` n `1226`
- 4h: commodity avg `0.1667` n `13`; crypto_alt avg `0.5831` n `238`; crypto_major avg `0.5728` n `8`; equity avg `1.2949` n `154`; fx avg `0.1376` n `6`; index avg `0.1653` n `27`; metal avg `-0.1256` n `20`; unknown avg `2.6288` n `1216`
- 24h: commodity avg `-0.0227` n `13`; crypto_alt avg `2.2546` n `237`; crypto_major avg `2.1046` n `8`; equity avg `2.7244` n `154`; fx avg `0.0678` n `6`; index avg `0.5013` n `27`; metal avg `0.1625` n `20`; unknown avg `100.6093` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
