# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T01:07:28.418064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0476` n `230`; crypto_major avg `0.0997` n `8`; equity avg `0.0253` n `113`; fx avg `-0.0121` n `6`; index avg `0.0069` n `25`; metal avg `0.0495` n `20`; unknown avg `-0.0367` n `786`
- 1h: commodity avg `0.0624` n `12`; crypto_alt avg `0.2038` n `230`; crypto_major avg `0.2689` n `8`; equity avg `0.1013` n `113`; fx avg `-0.0097` n `6`; index avg `0.0224` n `25`; metal avg `0.1002` n `20`; unknown avg `-0.0137` n `786`
- 4h: commodity avg `0.1692` n `12`; crypto_alt avg `0.2366` n `230`; crypto_major avg `0.3707` n `8`; equity avg `0.2078` n `113`; fx avg `0.0006` n `6`; index avg `0.0103` n `25`; metal avg `0.096` n `20`; unknown avg `-0.0899` n `785`
- 24h: commodity avg `0.2289` n `12`; crypto_alt avg `-1.1133` n `230`; crypto_major avg `1.0464` n `8`; equity avg `1.4689` n `113`; fx avg `0.0029` n `6`; index avg `0.1413` n `25`; metal avg `-0.2246` n `20`; unknown avg `-0.0455` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2269`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2203`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2173`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
