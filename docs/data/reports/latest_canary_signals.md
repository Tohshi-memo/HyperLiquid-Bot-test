# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T21:58:27.527215+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0315` n `12`; crypto_alt avg `-0.1551` n `230`; crypto_major avg `0.0065` n `8`; equity avg `-0.0177` n `113`; fx avg `0.0045` n `6`; index avg `0.0031` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.0691` n `786`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.7242` n `230`; crypto_major avg `-0.3864` n `8`; equity avg `0.0724` n `113`; fx avg `-0.0087` n `6`; index avg `0.0188` n `25`; metal avg `-0.0103` n `20`; unknown avg `-0.1462` n `786`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `-1.095` n `230`; crypto_major avg `-0.6162` n `8`; equity avg `-0.3796` n `113`; fx avg `-0.0092` n `6`; index avg `0.0059` n `25`; metal avg `-0.0453` n `20`; unknown avg `-0.3445` n `786`
- 24h: commodity avg `0.0222` n `12`; crypto_alt avg `-1.5946` n `230`; crypto_major avg `-0.5045` n `8`; equity avg `2.9079` n `113`; fx avg `0.028` n `6`; index avg `0.4023` n `25`; metal avg `0.1617` n `20`; unknown avg `-0.0551` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2345`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
