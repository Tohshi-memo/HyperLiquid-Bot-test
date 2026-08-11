# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T07:52:26.366343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `-0.0451` n `230`; crypto_major avg `0.038` n `8`; equity avg `-0.0282` n `113`; fx avg `0.0053` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.0344` n `785`
- 1h: commodity avg `0.0772` n `12`; crypto_alt avg `-0.1436` n `230`; crypto_major avg `0.1407` n `8`; equity avg `0.1199` n `113`; fx avg `-0.0144` n `6`; index avg `0.0119` n `25`; metal avg `-0.0084` n `20`; unknown avg `0.0378` n `785`
- 4h: commodity avg `0.3703` n `12`; crypto_alt avg `-0.5631` n `230`; crypto_major avg `-0.2165` n `8`; equity avg `-0.3124` n `113`; fx avg `0.0115` n `6`; index avg `-0.0574` n `25`; metal avg `-0.3402` n `20`; unknown avg `-0.0303` n `753`
- 24h: commodity avg `1.2722` n `12`; crypto_alt avg `-1.3605` n `230`; crypto_major avg `-1.1009` n `8`; equity avg `-1.476` n `113`; fx avg `0.037` n `6`; index avg `-0.0558` n `25`; metal avg `0.0349` n `20`; unknown avg `0.1497` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
