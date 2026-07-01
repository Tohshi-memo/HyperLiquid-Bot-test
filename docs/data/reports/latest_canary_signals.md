# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T02:52:25.667010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0156` n `12`; crypto_alt avg `0.0531` n `228`; crypto_major avg `-0.0321` n `8`; equity avg `0.0954` n `88`; fx avg `0.0056` n `6`; index avg `0.0214` n `23`; metal avg `-0.0788` n `20`; unknown avg `-0.0245` n `765`
- 1h: commodity avg `0.0197` n `12`; crypto_alt avg `0.6012` n `228`; crypto_major avg `0.5288` n `8`; equity avg `0.087` n `88`; fx avg `-0.012` n `6`; index avg `-0.0009` n `23`; metal avg `0.0149` n `20`; unknown avg `0.9276` n `765`
- 4h: commodity avg `-0.0592` n `12`; crypto_alt avg `0.6034` n `228`; crypto_major avg `0.776` n `8`; equity avg `-0.603` n `88`; fx avg `0.0796` n `6`; index avg `-0.2296` n `23`; metal avg `-0.4557` n `20`; unknown avg `0.1658` n `765`
- 24h: commodity avg `0.0213` n `12`; crypto_alt avg `-1.1591` n `228`; crypto_major avg `-0.773` n `8`; equity avg `0.508` n `88`; fx avg `0.1526` n `6`; index avg `0.0157` n `23`; metal avg `-0.0699` n `20`; unknown avg `7.0397` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
