# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T05:22:29.147808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `0.0056` n `230`; crypto_major avg `0.0092` n `8`; equity avg `-0.0338` n `102`; fx avg `0.014` n `6`; index avg `0.0051` n `25`; metal avg `-0.0268` n `20`; unknown avg `0.2114` n `784`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `-0.1455` n `230`; crypto_major avg `-0.1909` n `8`; equity avg `-0.2256` n `102`; fx avg `-0.0034` n `6`; index avg `-0.0474` n `25`; metal avg `-0.0452` n `20`; unknown avg `0.0564` n `784`
- 4h: commodity avg `-0.209` n `12`; crypto_alt avg `-0.2586` n `230`; crypto_major avg `-0.3699` n `8`; equity avg `0.0357` n `102`; fx avg `0.0084` n `6`; index avg `0.0432` n `25`; metal avg `0.0402` n `20`; unknown avg `0.0463` n `784`
- 24h: commodity avg `-0.3048` n `12`; crypto_alt avg `-0.9404` n `230`; crypto_major avg `-0.72` n `8`; equity avg `0.7254` n `102`; fx avg `-0.2104` n `6`; index avg `-0.0058` n `25`; metal avg `-0.0698` n `20`; unknown avg `0.9965` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
