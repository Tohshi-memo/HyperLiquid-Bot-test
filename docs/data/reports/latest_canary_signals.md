# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T11:37:26.241784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `12`; crypto_alt avg `-0.1886` n `230`; crypto_major avg `-0.1355` n `8`; equity avg `-0.057` n `102`; fx avg `0.0097` n `6`; index avg `0.0014` n `25`; metal avg `-0.0534` n `20`; unknown avg `0.1177` n `780`
- 1h: commodity avg `0.1249` n `12`; crypto_alt avg `-0.1996` n `230`; crypto_major avg `-0.0223` n `8`; equity avg `-0.013` n `102`; fx avg `0.0373` n `6`; index avg `-0.0552` n `25`; metal avg `-0.0717` n `20`; unknown avg `2.6206` n `780`
- 4h: commodity avg `0.4474` n `12`; crypto_alt avg `-0.3281` n `230`; crypto_major avg `-0.1807` n `8`; equity avg `0.388` n `102`; fx avg `0.0375` n `6`; index avg `-0.0369` n `25`; metal avg `-0.1438` n `20`; unknown avg `0.6676` n `779`
- 24h: commodity avg `0.4579` n `12`; crypto_alt avg `-0.4637` n `230`; crypto_major avg `-0.256` n `8`; equity avg `7.0692` n `102`; fx avg `-0.0541` n `6`; index avg `1.002` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.6787` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
