# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T12:51:30.057356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `-0.0405` n `232`; crypto_major avg `-0.0557` n `8`; equity avg `-0.0027` n `134`; fx avg `-0.0023` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0039` n `20`; unknown avg `145.2139` n `792`
- 1h: commodity avg `0.0128` n `12`; crypto_alt avg `-0.2116` n `232`; crypto_major avg `0.1068` n `8`; equity avg `0.0609` n `134`; fx avg `0.0023` n `6`; index avg `0.0041` n `26`; metal avg `-0.0019` n `20`; unknown avg `61.4632` n `784`
- 4h: commodity avg `-0.02` n `12`; crypto_alt avg `0.7548` n `232`; crypto_major avg `0.5584` n `8`; equity avg `0.2245` n `134`; fx avg `-0.0007` n `6`; index avg `0.0134` n `26`; metal avg `0.0046` n `20`; unknown avg `354.3197` n `784`
- 24h: commodity avg `0.1084` n `12`; crypto_alt avg `1.8266` n `232`; crypto_major avg `1.6323` n `8`; equity avg `0.561` n `134`; fx avg `-0.024` n `6`; index avg `0.0609` n `26`; metal avg `0.0145` n `20`; unknown avg `491.8896` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
