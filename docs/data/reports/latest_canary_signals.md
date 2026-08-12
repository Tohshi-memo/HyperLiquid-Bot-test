# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T05:37:27.307247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0323` n `12`; crypto_alt avg `-0.0808` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `0.1242` n `113`; fx avg `0.0065` n `6`; index avg `0.0414` n `25`; metal avg `0.0073` n `20`; unknown avg `-0.0645` n `786`
- 1h: commodity avg `-0.038` n `12`; crypto_alt avg `0.003` n `230`; crypto_major avg `0.133` n `8`; equity avg `-0.0473` n `113`; fx avg `-0.0029` n `6`; index avg `0.0005` n `25`; metal avg `-0.0324` n `20`; unknown avg `0.0626` n `786`
- 4h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.049` n `230`; crypto_major avg `0.0574` n `8`; equity avg `0.5033` n `113`; fx avg `0.0043` n `6`; index avg `0.0882` n `25`; metal avg `0.0761` n `20`; unknown avg `-0.2491` n `786`
- 24h: commodity avg `0.2501` n `12`; crypto_alt avg `-1.0528` n `230`; crypto_major avg `0.7165` n `8`; equity avg `1.7115` n `113`; fx avg `0.0062` n `6`; index avg `0.1337` n `25`; metal avg `0.1252` n `20`; unknown avg `-0.0658` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2245`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2198`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2144`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
