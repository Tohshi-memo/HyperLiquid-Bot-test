# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T01:52:27.911978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `0.0691` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `0.2002` n `102`; fx avg `-0.0076` n `6`; index avg `0.0799` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0574` n `784`
- 1h: commodity avg `-0.1285` n `12`; crypto_alt avg `-0.2082` n `230`; crypto_major avg `-0.2366` n `8`; equity avg `0.0444` n `102`; fx avg `0.0115` n `6`; index avg `0.0437` n `25`; metal avg `0.0281` n `20`; unknown avg `-0.1133` n `784`
- 4h: commodity avg `-0.0011` n `12`; crypto_alt avg `-0.9167` n `230`; crypto_major avg `-0.8883` n `8`; equity avg `0.1622` n `102`; fx avg `-0.2866` n `6`; index avg `-0.0903` n `25`; metal avg `-0.2729` n `20`; unknown avg `0.2013` n `783`
- 24h: commodity avg `-1.0198` n `12`; crypto_alt avg `-0.0159` n `230`; crypto_major avg `0.5302` n `8`; equity avg `1.5653` n `102`; fx avg `-0.2722` n `6`; index avg `0.1954` n `25`; metal avg `0.0911` n `20`; unknown avg `1.4473` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
