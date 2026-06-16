# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T09:52:38.682158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2105` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `0.0147` n `8`; equity avg `-0.0285` n `77`; fx avg `0.0055` n `6`; index avg `-0.0233` n `23`; metal avg `-0.0351` n `18`; unknown avg `-0.0798` n `687`
- 1h: commodity avg `0.37` n `12`; crypto_alt avg `-0.358` n `228`; crypto_major avg `-0.3788` n `8`; equity avg `-0.0981` n `77`; fx avg `0.0145` n `6`; index avg `-0.0518` n `23`; metal avg `0.1041` n `18`; unknown avg `0.1102` n `687`
- 4h: commodity avg `-0.207` n `12`; crypto_alt avg `0.9561` n `228`; crypto_major avg `1.0968` n `8`; equity avg `0.6101` n `77`; fx avg `0.0452` n `6`; index avg `0.1327` n `23`; metal avg `1.0384` n `18`; unknown avg `0.3074` n `647`
- 24h: commodity avg `0.4379` n `12`; crypto_alt avg `1.3575` n `228`; crypto_major avg `3.3488` n `8`; equity avg `1.7398` n `76`; fx avg `-0.0727` n `6`; index avg `0.51` n `23`; metal avg `0.2112` n `18`; unknown avg `0.3375` n `623`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
