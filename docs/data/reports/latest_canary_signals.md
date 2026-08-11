# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T11:22:34.251004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0616` n `12`; crypto_alt avg `-0.0451` n `230`; crypto_major avg `-0.052` n `8`; equity avg `-0.1179` n `113`; fx avg `-0.0042` n `6`; index avg `-0.027` n `25`; metal avg `-0.0315` n `20`; unknown avg `-0.066` n `785`
- 1h: commodity avg `-0.3742` n `12`; crypto_alt avg `0.2291` n `230`; crypto_major avg `0.2819` n `8`; equity avg `0.4089` n `113`; fx avg `-0.0501` n `6`; index avg `0.0635` n `25`; metal avg `0.0522` n `20`; unknown avg `-0.0121` n `785`
- 4h: commodity avg `-0.4327` n `12`; crypto_alt avg `0.2065` n `230`; crypto_major avg `0.7102` n `8`; equity avg `0.4634` n `113`; fx avg `-0.073` n `6`; index avg `0.1135` n `25`; metal avg `0.2875` n `20`; unknown avg `0.018` n `785`
- 24h: commodity avg `0.566` n `12`; crypto_alt avg `-1.1857` n `230`; crypto_major avg `-0.4388` n `8`; equity avg `-0.5859` n `113`; fx avg `-0.0393` n `6`; index avg `0.1091` n `25`; metal avg `0.4726` n `20`; unknown avg `0.1003` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1691`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
