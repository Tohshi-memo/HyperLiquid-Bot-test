# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T22:07:26.117118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2027` n `12`; crypto_alt avg `0.3136` n `234`; crypto_major avg `0.383` n `8`; equity avg `0.1335` n `140`; fx avg `0.0631` n `6`; index avg `0.0128` n `26`; metal avg `0.0787` n `20`; unknown avg `0.0947` n `915`
- 1h: commodity avg `-0.219` n `12`; crypto_alt avg `0.6765` n `234`; crypto_major avg `0.3553` n `8`; equity avg `0.1227` n `140`; fx avg `0.0115` n `6`; index avg `0.0041` n `26`; metal avg `0.0666` n `20`; unknown avg `0.0595` n `897`
- 4h: commodity avg `-0.2145` n `12`; crypto_alt avg `0.6579` n `234`; crypto_major avg `0.2952` n `8`; equity avg `0.1949` n `140`; fx avg `0.0201` n `6`; index avg `0.0263` n `26`; metal avg `0.0515` n `20`; unknown avg `0.4836` n `847`
- 24h: commodity avg `0.1189` n `12`; crypto_alt avg `1.9613` n `234`; crypto_major avg `0.5844` n `8`; equity avg `0.0593` n `140`; fx avg `0.0148` n `6`; index avg `-0.0307` n `26`; metal avg `0.0241` n `20`; unknown avg `2.703` n `751`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
