# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T07:37:25.414019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `-0.1084` n `230`; crypto_major avg `-0.2907` n `8`; equity avg `0.0207` n `121`; fx avg `-0.0766` n `6`; index avg `0.0027` n `25`; metal avg `0.0072` n `20`; unknown avg `0.0111` n `794`
- 1h: commodity avg `-0.0001` n `12`; crypto_alt avg `0.3571` n `230`; crypto_major avg `-0.1165` n `8`; equity avg `0.0401` n `121`; fx avg `0.0568` n `6`; index avg `-0.0016` n `25`; metal avg `0.0256` n `20`; unknown avg `0.1102` n `794`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `0.271` n `230`; crypto_major avg `-0.7283` n `8`; equity avg `-0.1299` n `121`; fx avg `0.0835` n `6`; index avg `-0.0326` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.4134` n `778`
- 24h: commodity avg `-0.0047` n `12`; crypto_alt avg `-3.991` n `230`; crypto_major avg `-2.8475` n `8`; equity avg `-0.0844` n `121`; fx avg `0.1915` n `6`; index avg `-0.0247` n `25`; metal avg `0.0599` n `20`; unknown avg `2.3098` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
