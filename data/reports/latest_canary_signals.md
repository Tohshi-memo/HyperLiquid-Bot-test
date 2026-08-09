# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T22:07:31.886770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3198` n `12`; crypto_alt avg `0.0705` n `230`; crypto_major avg `0.0485` n `8`; equity avg `-0.1339` n `112`; fx avg `0.0038` n `6`; index avg `-0.0426` n `25`; metal avg `-0.0868` n `20`; unknown avg `-0.068` n `785`
- 1h: commodity avg `0.4274` n `12`; crypto_alt avg `0.1074` n `230`; crypto_major avg `0.1371` n `8`; equity avg `-0.122` n `112`; fx avg `-0.0173` n `6`; index avg `-0.0421` n `25`; metal avg `-0.1663` n `20`; unknown avg `0.0169` n `785`
- 4h: commodity avg `0.5428` n `12`; crypto_alt avg `0.179` n `230`; crypto_major avg `0.017` n `8`; equity avg `-0.0662` n `112`; fx avg `-0.0042` n `6`; index avg `-0.036` n `25`; metal avg `-0.138` n `20`; unknown avg `-0.4779` n `785`
- 24h: commodity avg `0.5194` n `12`; crypto_alt avg `1.5174` n `230`; crypto_major avg `0.345` n `8`; equity avg `0.0986` n `112`; fx avg `-0.0044` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0751` n `20`; unknown avg `-0.2854` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
