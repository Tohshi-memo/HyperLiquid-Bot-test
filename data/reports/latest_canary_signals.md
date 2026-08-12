# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T21:37:28.633205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `-0.5581` n `230`; crypto_major avg `-0.3307` n `8`; equity avg `0.0073` n `113`; fx avg `0.0036` n `6`; index avg `0.0033` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0973` n `786`
- 1h: commodity avg `0.028` n `12`; crypto_alt avg `-0.7259` n `230`; crypto_major avg `-0.4534` n `8`; equity avg `0.1312` n `113`; fx avg `-0.0123` n `6`; index avg `0.0167` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.2401` n `786`
- 4h: commodity avg `-0.0593` n `12`; crypto_alt avg `-0.9865` n `230`; crypto_major avg `-0.6147` n `8`; equity avg `-0.2081` n `113`; fx avg `-0.0249` n `6`; index avg `0.0103` n `25`; metal avg `-0.0444` n `20`; unknown avg `0.3405` n `786`
- 24h: commodity avg `0.061` n `12`; crypto_alt avg `-1.4234` n `230`; crypto_major avg `-0.4462` n `8`; equity avg `2.9387` n `113`; fx avg `0.0208` n `6`; index avg `0.3773` n `25`; metal avg `0.1646` n `20`; unknown avg `0.0128` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2345`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
