# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T01:22:23.941461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.0783` n `230`; crypto_major avg `0.1121` n `8`; equity avg `0.3664` n `113`; fx avg `0.0169` n `6`; index avg `0.0925` n `25`; metal avg `0.0878` n `20`; unknown avg `-0.0347` n `785`
- 1h: commodity avg `0.0137` n `12`; crypto_alt avg `0.1467` n `230`; crypto_major avg `0.1014` n `8`; equity avg `0.4739` n `113`; fx avg `-0.0589` n `6`; index avg `0.1349` n `25`; metal avg `0.0788` n `20`; unknown avg `-0.0699` n `785`
- 4h: commodity avg `-0.0445` n `12`; crypto_alt avg `0.2958` n `230`; crypto_major avg `-0.1711` n `8`; equity avg `0.4094` n `113`; fx avg `-0.0543` n `6`; index avg `0.0825` n `25`; metal avg `0.1768` n `20`; unknown avg `-0.2665` n `785`
- 24h: commodity avg `0.7929` n `12`; crypto_alt avg `-0.4499` n `230`; crypto_major avg `-0.6599` n `8`; equity avg `-1.2222` n `113`; fx avg `0.1059` n `6`; index avg `-0.0005` n `25`; metal avg `0.6856` n `20`; unknown avg `103.8338` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
