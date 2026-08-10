# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T08:22:34.094252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `-0.016` n `230`; crypto_major avg `0.0459` n `8`; equity avg `-0.0687` n `112`; fx avg `0.0085` n `6`; index avg `-0.0203` n `25`; metal avg `-0.0158` n `20`; unknown avg `0.0036` n `785`
- 1h: commodity avg `0.0224` n `12`; crypto_alt avg `0.0487` n `230`; crypto_major avg `0.0503` n `8`; equity avg `0.0737` n `112`; fx avg `0.0235` n `6`; index avg `0.0121` n `25`; metal avg `-0.0294` n `20`; unknown avg `0.0443` n `785`
- 4h: commodity avg `0.0118` n `12`; crypto_alt avg `0.2728` n `230`; crypto_major avg `0.4647` n `8`; equity avg `0.2343` n `112`; fx avg `0.1027` n `6`; index avg `0.0474` n `25`; metal avg `0.0479` n `20`; unknown avg `57.2554` n `753`
- 24h: commodity avg `0.3749` n `12`; crypto_alt avg `0.9241` n `230`; crypto_major avg `0.3028` n `8`; equity avg `0.0014` n `112`; fx avg `0.2146` n `6`; index avg `0.0748` n `25`; metal avg `-0.0485` n `20`; unknown avg `56.9898` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
