# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T06:52:34.436897+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0642` n `12`; crypto_alt avg `-0.0698` n `230`; crypto_major avg `-0.091` n `8`; equity avg `-0.0099` n `108`; fx avg `0.0209` n `6`; index avg `0.0066` n `25`; metal avg `0.0039` n `20`; unknown avg `-0.021` n `781`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `0.009` n `230`; crypto_major avg `-0.0322` n `8`; equity avg `-0.2087` n `108`; fx avg `0.0133` n `6`; index avg `-0.0195` n `25`; metal avg `0.0938` n `20`; unknown avg `-0.0011` n `749`
- 4h: commodity avg `0.1355` n `12`; crypto_alt avg `0.1757` n `230`; crypto_major avg `-0.0679` n `8`; equity avg `0.4834` n `108`; fx avg `0.046` n `6`; index avg `0.0578` n `25`; metal avg `0.3272` n `20`; unknown avg `0.058` n `749`
- 24h: commodity avg `-1.3437` n `12`; crypto_alt avg `0.895` n `230`; crypto_major avg `1.0966` n `8`; equity avg `3.5231` n `108`; fx avg `-0.0405` n `6`; index avg `0.7388` n `25`; metal avg `1.3723` n `20`; unknown avg `0.5143` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
