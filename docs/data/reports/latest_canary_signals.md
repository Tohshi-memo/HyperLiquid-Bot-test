# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T20:52:28.989020+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.0796` n `234`; crypto_major avg `0.048` n `8`; equity avg `0.0081` n `140`; fx avg `0.0054` n `6`; index avg `-0.0083` n `26`; metal avg `0.0064` n `20`; unknown avg `1.3228` n `939`
- 1h: commodity avg `-0.0164` n `12`; crypto_alt avg `0.1228` n `234`; crypto_major avg `-0.2747` n `8`; equity avg `0.0392` n `140`; fx avg `0.0077` n `6`; index avg `0.0124` n `26`; metal avg `-0.0086` n `20`; unknown avg `5.1413` n `901`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `0.4187` n `234`; crypto_major avg `-0.0227` n `8`; equity avg `0.0786` n `140`; fx avg `-0.0202` n `6`; index avg `0.0098` n `26`; metal avg `-0.0333` n `20`; unknown avg `1.4734` n `881`
- 24h: commodity avg `0.3694` n `12`; crypto_alt avg `0.7915` n `234`; crypto_major avg `-0.2138` n `8`; equity avg `-0.0697` n `140`; fx avg `0.0242` n `6`; index avg `-0.0181` n `26`; metal avg `-0.0391` n `20`; unknown avg `2.4741` n `793`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
