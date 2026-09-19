# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T19:00:28.055824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.1734` n `234`; crypto_major avg `0.0891` n `8`; equity avg `0.0036` n `140`; fx avg `-0.0011` n `6`; index avg `-0.0005` n `26`; metal avg `0.0031` n `20`; unknown avg `1.7506` n `941`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `-0.0928` n `234`; crypto_major avg `-0.108` n `8`; equity avg `0.043` n `140`; fx avg `-0.0061` n `6`; index avg `0.0004` n `26`; metal avg `0.0091` n `20`; unknown avg `1.8405` n `941`
- 4h: commodity avg `-0.0141` n `12`; crypto_alt avg `-0.1336` n `234`; crypto_major avg `-0.4101` n `8`; equity avg `0.0617` n `140`; fx avg `-0.022` n `6`; index avg `0.0216` n `26`; metal avg `-0.0096` n `20`; unknown avg `7.6134` n `883`
- 24h: commodity avg `0.094` n `12`; crypto_alt avg `1.9547` n `234`; crypto_major avg `0.725` n `8`; equity avg `0.3558` n `140`; fx avg `0.0117` n `6`; index avg `0.0779` n `26`; metal avg `-0.0347` n `20`; unknown avg `6.9181` n `792`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
