# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T11:07:20.225027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1042` n `12`; crypto_alt avg `-0.0403` n `228`; crypto_major avg `-0.0746` n `8`; equity avg `-0.0156` n `67`; fx avg `0.0202` n `6`; index avg `-0.0137` n `23`; metal avg `-0.0638` n `18`; unknown avg `-0.0558` n `397`
- 1h: commodity avg `0.0114` n `12`; crypto_alt avg `0.2177` n `228`; crypto_major avg `-0.0802` n `8`; equity avg `0.0229` n `67`; fx avg `0.0197` n `6`; index avg `0.0273` n `23`; metal avg `-0.0514` n `18`; unknown avg `-0.0972` n `397`
- 4h: commodity avg `0.0031` n `12`; crypto_alt avg `0.4017` n `228`; crypto_major avg `0.2259` n `8`; equity avg `0.2541` n `67`; fx avg `0.0532` n `6`; index avg `0.0368` n `23`; metal avg `0.2212` n `18`; unknown avg `-0.0144` n `397`
- 24h: commodity avg `-0.0912` n `12`; crypto_alt avg `0.5223` n `228`; crypto_major avg `-0.1874` n `8`; equity avg `0.4807` n `67`; fx avg `0.0196` n `6`; index avg `-0.0169` n `23`; metal avg `0.6533` n `18`; unknown avg `0.8296` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
