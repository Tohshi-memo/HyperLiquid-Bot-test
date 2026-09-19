# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T02:52:28.127049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.0704` n `234`; crypto_major avg `-0.1626` n `8`; equity avg `0.0047` n `140`; fx avg `-0.0025` n `6`; index avg `0.0123` n `26`; metal avg `0.0051` n `20`; unknown avg `0.2954` n `942`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.6101` n `234`; crypto_major avg `0.2011` n `8`; equity avg `-0.0078` n `140`; fx avg `0.0022` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0071` n `20`; unknown avg `3.571` n `940`
- 4h: commodity avg `0.1676` n `12`; crypto_alt avg `0.9006` n `234`; crypto_major avg `0.5349` n `8`; equity avg `-0.0557` n `140`; fx avg `-0.0019` n `6`; index avg `0.0055` n `26`; metal avg `-0.0307` n `20`; unknown avg `0.4248` n `934`
- 24h: commodity avg `0.1216` n `12`; crypto_alt avg `5.6984` n `234`; crypto_major avg `6.1247` n `8`; equity avg `1.1893` n `140`; fx avg `0.1763` n `6`; index avg `0.1167` n `26`; metal avg `0.1335` n `20`; unknown avg `4.2633` n `787`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
