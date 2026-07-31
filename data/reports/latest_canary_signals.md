# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T17:52:55.981953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.0348` n `230`; crypto_major avg `0.079` n `8`; equity avg `-0.1026` n `102`; fx avg `0.0071` n `6`; index avg `-0.0131` n `25`; metal avg `0.0273` n `20`; unknown avg `0.0045` n `780`
- 1h: commodity avg `0.058` n `12`; crypto_alt avg `0.4259` n `230`; crypto_major avg `0.3947` n `8`; equity avg `0.5236` n `102`; fx avg `-0.0367` n `6`; index avg `0.0707` n `25`; metal avg `0.1532` n `20`; unknown avg `0.2245` n `780`
- 4h: commodity avg `-0.1211` n `12`; crypto_alt avg `0.857` n `230`; crypto_major avg `0.1031` n `8`; equity avg `0.138` n `102`; fx avg `0.0674` n `6`; index avg `0.1067` n `25`; metal avg `0.3347` n `20`; unknown avg `0.0342` n `780`
- 24h: commodity avg `0.129` n `12`; crypto_alt avg `-0.066` n `230`; crypto_major avg `-1.6346` n `8`; equity avg `0.7853` n `102`; fx avg `0.1707` n `6`; index avg `0.3401` n `25`; metal avg `-0.2339` n `20`; unknown avg `0.462` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
