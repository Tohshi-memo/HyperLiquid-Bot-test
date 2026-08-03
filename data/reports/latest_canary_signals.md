# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T12:22:42.487239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `0.1163` n `230`; crypto_major avg `0.2114` n `8`; equity avg `0.2447` n `102`; fx avg `-0.008` n `6`; index avg `0.0385` n `25`; metal avg `-0.0976` n `20`; unknown avg `0.0441` n `785`
- 1h: commodity avg `-0.0655` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `-0.1216` n `8`; equity avg `-0.2876` n `102`; fx avg `-0.0119` n `6`; index avg `-0.0649` n `25`; metal avg `-0.089` n `20`; unknown avg `0.0032` n `785`
- 4h: commodity avg `-0.179` n `12`; crypto_alt avg `0.4512` n `230`; crypto_major avg `0.4876` n `8`; equity avg `-0.8698` n `102`; fx avg `-0.0293` n `6`; index avg `-0.1388` n `25`; metal avg `-0.2443` n `20`; unknown avg `0.3352` n `784`
- 24h: commodity avg `-0.3635` n `12`; crypto_alt avg `-0.7353` n `230`; crypto_major avg `-0.1585` n `8`; equity avg `-0.8501` n `102`; fx avg `-0.2122` n `6`; index avg `-0.1875` n `25`; metal avg `-0.3265` n `20`; unknown avg `1.2866` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
