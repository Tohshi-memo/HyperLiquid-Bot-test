# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T06:22:58.392798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `12`; crypto_alt avg `-0.1326` n `230`; crypto_major avg `-0.1221` n `8`; equity avg `0.0037` n `102`; fx avg `0.0325` n `6`; index avg `0.0207` n `25`; metal avg `0.0803` n `20`; unknown avg `0.0311` n `784`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `0.0925` n `230`; crypto_major avg `0.0449` n `8`; equity avg `0.0602` n `102`; fx avg `-0.0207` n `6`; index avg `0.017` n `25`; metal avg `0.1407` n `20`; unknown avg `0.008` n `768`
- 4h: commodity avg `-0.1157` n `12`; crypto_alt avg `-0.3081` n `230`; crypto_major avg `-0.4234` n `8`; equity avg `-0.2639` n `102`; fx avg `0.0035` n `6`; index avg `-0.0517` n `25`; metal avg `0.1301` n `20`; unknown avg `0.0507` n `768`
- 24h: commodity avg `-0.2297` n `12`; crypto_alt avg `-0.886` n `230`; crypto_major avg `-0.5406` n `8`; equity avg `0.7557` n `102`; fx avg `-0.2325` n `6`; index avg `-0.007` n `25`; metal avg `0.065` n `20`; unknown avg `0.9793` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
