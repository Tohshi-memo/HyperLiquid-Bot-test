# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T08:52:29.408076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.048` n `12`; crypto_alt avg `0.0717` n `230`; crypto_major avg `0.1648` n `8`; equity avg `0.0007` n `108`; fx avg `-0.0083` n `6`; index avg `-0.0045` n `25`; metal avg `0.0445` n `20`; unknown avg `0.0836` n `782`
- 1h: commodity avg `-0.1213` n `12`; crypto_alt avg `0.0596` n `230`; crypto_major avg `0.2515` n `8`; equity avg `0.0337` n `108`; fx avg `-0.0413` n `6`; index avg `0.0221` n `25`; metal avg `0.2157` n `20`; unknown avg `0.0079` n `782`
- 4h: commodity avg `0.0818` n `12`; crypto_alt avg `0.2672` n `230`; crypto_major avg `0.2559` n `8`; equity avg `-0.171` n `108`; fx avg `0.0729` n `6`; index avg `-0.0342` n `25`; metal avg `0.1012` n `20`; unknown avg `0.0019` n `750`
- 24h: commodity avg `-0.3211` n `12`; crypto_alt avg `0.3428` n `230`; crypto_major avg `-0.0678` n `8`; equity avg `-1.318` n `108`; fx avg `0.0062` n `6`; index avg `-0.295` n `25`; metal avg `0.505` n `20`; unknown avg `0.8236` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
