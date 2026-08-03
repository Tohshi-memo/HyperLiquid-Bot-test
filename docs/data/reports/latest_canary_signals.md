# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T13:22:28.599575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `12`; crypto_alt avg `0.4216` n `230`; crypto_major avg `0.3466` n `8`; equity avg `0.0731` n `102`; fx avg `-0.0262` n `6`; index avg `0.0256` n `25`; metal avg `-0.0602` n `20`; unknown avg `0.0837` n `785`
- 1h: commodity avg `0.0392` n `12`; crypto_alt avg `0.4366` n `230`; crypto_major avg `0.36` n `8`; equity avg `0.0989` n `102`; fx avg `0.0032` n `6`; index avg `0.0371` n `25`; metal avg `-0.2556` n `20`; unknown avg `0.1043` n `785`
- 4h: commodity avg `-0.0872` n `12`; crypto_alt avg `0.5166` n `230`; crypto_major avg `0.412` n `8`; equity avg `-1.0557` n `102`; fx avg `-0.044` n `6`; index avg `-0.1242` n `25`; metal avg `-0.5016` n `20`; unknown avg `0.3462` n `784`
- 24h: commodity avg `-0.4132` n `12`; crypto_alt avg `-0.1596` n `230`; crypto_major avg `0.2436` n `8`; equity avg `-0.7839` n `102`; fx avg `-0.2067` n `6`; index avg `-0.1639` n `25`; metal avg `-0.6014` n `20`; unknown avg `1.379` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
