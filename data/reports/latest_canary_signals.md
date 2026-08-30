# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T20:07:32.404347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0825` n `12`; crypto_alt avg `0.0792` n `231`; crypto_major avg `0.0472` n `8`; equity avg `-0.01` n `128`; fx avg `0.0` n `6`; index avg `0.0037` n `26`; metal avg `-0.0096` n `20`; unknown avg `-0.1314` n `791`
- 1h: commodity avg `0.3302` n `12`; crypto_alt avg `-0.3449` n `231`; crypto_major avg `-0.442` n `8`; equity avg `-0.0718` n `128`; fx avg `-0.0034` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.379` n `791`
- 4h: commodity avg `0.3778` n `12`; crypto_alt avg `0.3579` n `231`; crypto_major avg `0.0656` n `8`; equity avg `0.0295` n `128`; fx avg `-0.0007` n `6`; index avg `0.0134` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.235` n `791`
- 24h: commodity avg `0.4049` n `12`; crypto_alt avg `1.3993` n `231`; crypto_major avg `0.6485` n `8`; equity avg `0.1622` n `128`; fx avg `0.0285` n `6`; index avg `0.0494` n `26`; metal avg `0.083` n `20`; unknown avg `0.1438` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
