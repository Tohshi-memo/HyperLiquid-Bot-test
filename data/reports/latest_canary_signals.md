# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T08:22:26.382798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `12`; crypto_alt avg `-0.1888` n `232`; crypto_major avg `-0.1009` n `8`; equity avg `-0.078` n `134`; fx avg `0.0033` n `6`; index avg `-0.0198` n `26`; metal avg `-0.0413` n `20`; unknown avg `0.7787` n `797`
- 1h: commodity avg `0.0708` n `12`; crypto_alt avg `-0.1235` n `232`; crypto_major avg `-0.0116` n `8`; equity avg `-0.5252` n `134`; fx avg `-0.0217` n `6`; index avg `-0.0965` n `26`; metal avg `-0.1353` n `20`; unknown avg `0.9218` n `795`
- 4h: commodity avg `0.311` n `12`; crypto_alt avg `-0.2808` n `232`; crypto_major avg `-0.1395` n `8`; equity avg `-1.3629` n `134`; fx avg `0.0571` n `6`; index avg `-0.3283` n `26`; metal avg `-0.3176` n `20`; unknown avg `0.9172` n `747`
- 24h: commodity avg `0.637` n `12`; crypto_alt avg `0.285` n `232`; crypto_major avg `-0.9378` n `8`; equity avg `-0.7331` n `134`; fx avg `-0.0667` n `6`; index avg `-0.1804` n `26`; metal avg `-0.1189` n `20`; unknown avg `7508.6742` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
