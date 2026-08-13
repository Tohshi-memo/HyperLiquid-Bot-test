# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T03:52:29.341573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `12`; crypto_alt avg `0.0751` n `230`; crypto_major avg `0.0232` n `8`; equity avg `0.0735` n `113`; fx avg `0.0036` n `6`; index avg `0.0137` n `25`; metal avg `-0.0151` n `20`; unknown avg `0.2529` n `786`
- 1h: commodity avg `0.054` n `12`; crypto_alt avg `0.321` n `230`; crypto_major avg `0.2494` n `8`; equity avg `0.0314` n `113`; fx avg `0.0051` n `6`; index avg `0.0157` n `25`; metal avg `0.0056` n `20`; unknown avg `0.876` n `786`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `0.5745` n `230`; crypto_major avg `0.5365` n `8`; equity avg `0.4514` n `113`; fx avg `-0.0241` n `6`; index avg `0.0824` n `25`; metal avg `-0.0629` n `20`; unknown avg `0.1456` n `786`
- 24h: commodity avg `-0.2803` n `12`; crypto_alt avg `-1.1025` n `230`; crypto_major avg `-0.0961` n `8`; equity avg `2.4703` n `113`; fx avg `-0.0464` n `6`; index avg `0.308` n `25`; metal avg `-0.0918` n `20`; unknown avg `0.0115` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2408`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1933`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
