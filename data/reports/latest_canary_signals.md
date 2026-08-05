# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T01:52:33.127893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.0045` n `230`; crypto_major avg `0.1022` n `8`; equity avg `0.3021` n `108`; fx avg `-0.0019` n `6`; index avg `0.0331` n `25`; metal avg `0.0597` n `20`; unknown avg `-0.1663` n `781`
- 1h: commodity avg `0.1238` n `12`; crypto_alt avg `0.4202` n `230`; crypto_major avg `0.4915` n `8`; equity avg `0.2687` n `108`; fx avg `0.0012` n `6`; index avg `0.006` n `25`; metal avg `0.0467` n `20`; unknown avg `0.0534` n `781`
- 4h: commodity avg `0.1824` n `12`; crypto_alt avg `0.1596` n `230`; crypto_major avg `0.1134` n `8`; equity avg `0.7653` n `108`; fx avg `-0.0816` n `6`; index avg `0.0736` n `25`; metal avg `0.0732` n `20`; unknown avg `-0.174` n `781`
- 24h: commodity avg `-1.2255` n `12`; crypto_alt avg `0.113` n `230`; crypto_major avg `0.471` n `8`; equity avg `3.6175` n `107`; fx avg `0.0658` n `6`; index avg `0.7572` n `25`; metal avg `0.7927` n `20`; unknown avg `0.3538` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
