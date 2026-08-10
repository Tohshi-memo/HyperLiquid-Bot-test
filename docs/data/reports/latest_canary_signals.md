# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T22:17:27.156411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `12`; crypto_alt avg `0.2387` n `230`; crypto_major avg `0.1573` n `8`; equity avg `-0.0027` n `113`; fx avg `-0.0064` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0332` n `785`
- 1h: commodity avg `-0.0319` n `12`; crypto_alt avg `0.1337` n `230`; crypto_major avg `-0.0685` n `8`; equity avg `0.0548` n `113`; fx avg `-0.0021` n `6`; index avg `0.0027` n `25`; metal avg `-0.0204` n `20`; unknown avg `-0.1151` n `785`
- 4h: commodity avg `-0.1123` n `12`; crypto_alt avg `-0.3741` n `230`; crypto_major avg `0.0799` n `8`; equity avg `-0.3019` n `113`; fx avg `0.0095` n `6`; index avg `-0.0028` n `25`; metal avg `0.2154` n `20`; unknown avg `2.9597` n `785`
- 24h: commodity avg `0.8055` n `12`; crypto_alt avg `-1.5536` n `230`; crypto_major avg `-1.3617` n `8`; equity avg `-1.6697` n `113`; fx avg `0.2603` n `6`; index avg `-0.0507` n `25`; metal avg `0.3594` n `20`; unknown avg `103.6679` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
