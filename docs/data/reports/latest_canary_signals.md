# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T03:37:27.145858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0294` n `12`; crypto_alt avg `0.028` n `230`; crypto_major avg `0.0259` n `8`; equity avg `-0.0524` n `113`; fx avg `-0.0022` n `6`; index avg `-0.0074` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0646` n `786`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `0.3957` n `230`; crypto_major avg `0.3891` n `8`; equity avg `0.01` n `113`; fx avg `0.0048` n `6`; index avg `0.0167` n `25`; metal avg `0.0588` n `20`; unknown avg `0.4839` n `786`
- 4h: commodity avg `-0.0862` n `12`; crypto_alt avg `0.5658` n `230`; crypto_major avg `0.5312` n `8`; equity avg `0.3742` n `113`; fx avg `-0.0242` n `6`; index avg `0.0611` n `25`; metal avg `-0.0334` n `20`; unknown avg `-0.0535` n `786`
- 24h: commodity avg `-0.248` n `12`; crypto_alt avg `-1.3101` n `230`; crypto_major avg `-0.1684` n `8`; equity avg `2.3631` n `113`; fx avg `-0.0614` n `6`; index avg `0.2805` n `25`; metal avg `-0.0885` n `20`; unknown avg `-0.0086` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
