# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T18:22:28.753375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `-0.1753` n `234`; crypto_major avg `-0.1824` n `8`; equity avg `0.0186` n `140`; fx avg `-0.0035` n `6`; index avg `0.0027` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0908` n `943`
- 1h: commodity avg `0.0731` n `12`; crypto_alt avg `-0.5455` n `234`; crypto_major avg `-0.4633` n `8`; equity avg `0.0025` n `140`; fx avg `-0.0013` n `6`; index avg `0.0129` n `26`; metal avg `0.0135` n `20`; unknown avg `0.669` n `941`
- 4h: commodity avg `-0.0671` n `12`; crypto_alt avg `-0.2902` n `234`; crypto_major avg `-0.5253` n `8`; equity avg `0.0321` n `140`; fx avg `-0.0128` n `6`; index avg `0.0259` n `26`; metal avg `-0.0017` n `20`; unknown avg `5.9717` n `882`
- 24h: commodity avg `0.0152` n `12`; crypto_alt avg `2.1857` n `234`; crypto_major avg `0.8137` n `8`; equity avg `0.4614` n `140`; fx avg `0.0094` n `6`; index avg `0.1245` n `26`; metal avg `-0.132` n `20`; unknown avg `3.9286` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
