# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T19:37:25.270209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0195` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `0.0182` n `8`; equity avg `-0.0213` n `102`; fx avg `0.0305` n `6`; index avg `-0.0107` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0183` n `779`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `0.1223` n `230`; crypto_major avg `0.185` n `8`; equity avg `0.4673` n `102`; fx avg `0.0391` n `6`; index avg `0.0946` n `25`; metal avg `0.0885` n `20`; unknown avg `-0.0864` n `779`
- 4h: commodity avg `-0.1764` n `12`; crypto_alt avg `0.1145` n `230`; crypto_major avg `0.5204` n `8`; equity avg `0.968` n `102`; fx avg `-0.0253` n `6`; index avg `0.1764` n `25`; metal avg `0.2876` n `20`; unknown avg `-0.1586` n `779`
- 24h: commodity avg `-0.2242` n `12`; crypto_alt avg `0.6869` n `230`; crypto_major avg `1.6989` n `8`; equity avg `4.9667` n `102`; fx avg `-0.3803` n `6`; index avg `0.5286` n `25`; metal avg `0.5465` n `20`; unknown avg `0.0481` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
