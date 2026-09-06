# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T20:37:25.277682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `0.0733` n `232`; crypto_major avg `0.1546` n `8`; equity avg `-0.0219` n `134`; fx avg `0.0037` n `6`; index avg `0.0007` n `26`; metal avg `0.0018` n `20`; unknown avg `0.5697` n `787`
- 1h: commodity avg `-0.0382` n `12`; crypto_alt avg `0.3407` n `232`; crypto_major avg `0.2955` n `8`; equity avg `-0.0007` n `134`; fx avg `0.0019` n `6`; index avg `0.0107` n `26`; metal avg `0.0068` n `20`; unknown avg `-0.4272` n `775`
- 4h: commodity avg `-0.0704` n `12`; crypto_alt avg `0.1187` n `232`; crypto_major avg `0.2255` n `8`; equity avg `0.1883` n `134`; fx avg `0.0042` n `6`; index avg `0.0245` n `26`; metal avg `0.0375` n `20`; unknown avg `0.8702` n `755`
- 24h: commodity avg `-0.0083` n `12`; crypto_alt avg `1.3823` n `232`; crypto_major avg `0.3734` n `8`; equity avg `0.3657` n `134`; fx avg `-0.0021` n `6`; index avg `0.0146` n `26`; metal avg `-0.0108` n `20`; unknown avg `100.8236` n `676`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
