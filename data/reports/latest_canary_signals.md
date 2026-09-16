# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T20:52:34.611747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0359` n `12`; crypto_alt avg `0.1486` n `234`; crypto_major avg `0.0201` n `8`; equity avg `0.076` n `137`; fx avg `-0.0002` n `6`; index avg `0.0089` n `27`; metal avg `0.0037` n `20`; unknown avg `4.1558` n `919`
- 1h: commodity avg `0.073` n `12`; crypto_alt avg `0.4688` n `234`; crypto_major avg `0.051` n `8`; equity avg `0.2724` n `137`; fx avg `0.0338` n `6`; index avg `0.036` n `27`; metal avg `0.021` n `20`; unknown avg `7.0056` n `869`
- 4h: commodity avg `-0.0204` n `12`; crypto_alt avg `1.2294` n `234`; crypto_major avg `0.9106` n `8`; equity avg `-0.519` n `137`; fx avg `0.0759` n `6`; index avg `-0.1959` n `27`; metal avg `-0.5196` n `20`; unknown avg `7.544` n `829`
- 24h: commodity avg `-0.5913` n `12`; crypto_alt avg `-0.0977` n `234`; crypto_major avg `0.6587` n `8`; equity avg `0.7102` n `137`; fx avg `0.1053` n `6`; index avg `0.0194` n `27`; metal avg `-0.2816` n `20`; unknown avg `4.7719` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
