# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T06:06:29.066314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0414` n `12`; crypto_alt avg `0.1857` n `230`; crypto_major avg `0.1507` n `8`; equity avg `0.0679` n `112`; fx avg `0.0139` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0752` n `20`; unknown avg `0.1663` n `753`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `0.3308` n `230`; crypto_major avg `0.3213` n `8`; equity avg `0.0453` n `112`; fx avg `0.0189` n `6`; index avg `0.0018` n `25`; metal avg `0.0951` n `20`; unknown avg `0.0877` n `753`
- 4h: commodity avg `-0.1284` n `12`; crypto_alt avg `0.2098` n `230`; crypto_major avg `0.1532` n `8`; equity avg `-0.0455` n `112`; fx avg `0.0237` n `6`; index avg `-0.0023` n `25`; metal avg `0.1747` n `20`; unknown avg `0.137` n `753`
- 24h: commodity avg `0.2468` n `12`; crypto_alt avg `0.9074` n `230`; crypto_major avg `0.233` n `8`; equity avg `-0.2651` n `112`; fx avg `0.1501` n `6`; index avg `0.0247` n `25`; metal avg `-0.0149` n `20`; unknown avg `-0.1513` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
