# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T04:22:29.944775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0445` n `12`; crypto_alt avg `0.0002` n `230`; crypto_major avg `-0.0537` n `8`; equity avg `-0.1627` n `113`; fx avg `-0.0053` n `6`; index avg `-0.0511` n `25`; metal avg `-0.0202` n `20`; unknown avg `-0.1171` n `787`
- 1h: commodity avg `0.119` n `12`; crypto_alt avg `0.0534` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `-0.1058` n `113`; fx avg `-0.0019` n `6`; index avg `-0.0257` n `25`; metal avg `-0.0878` n `20`; unknown avg `-0.205` n `786`
- 4h: commodity avg `0.0589` n `12`; crypto_alt avg `0.0708` n `230`; crypto_major avg `0.2323` n `8`; equity avg `0.0138` n `113`; fx avg `0.019` n `6`; index avg `-0.0524` n `25`; metal avg `-0.309` n `20`; unknown avg `-0.3459` n `786`
- 24h: commodity avg `-0.1497` n `12`; crypto_alt avg `-1.1426` n `230`; crypto_major avg `-0.1661` n `8`; equity avg `2.3226` n `113`; fx avg `-0.0397` n `6`; index avg `0.2743` n `25`; metal avg `-0.1603` n `20`; unknown avg `-0.0166` n `770`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1915`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
