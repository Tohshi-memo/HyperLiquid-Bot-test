# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T09:52:30.008388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.0844` n `228`; crypto_major avg `-0.0398` n `8`; equity avg `0.0488` n `88`; fx avg `0.0084` n `6`; index avg `0.0107` n `23`; metal avg `-0.0014` n `20`; unknown avg `0.2528` n `765`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `0.3542` n `228`; crypto_major avg `0.2962` n `8`; equity avg `0.0602` n `88`; fx avg `0.0243` n `6`; index avg `-0.0037` n `23`; metal avg `0.0773` n `20`; unknown avg `0.3629` n `765`
- 4h: commodity avg `-0.2015` n `12`; crypto_alt avg `-0.3986` n `228`; crypto_major avg `-0.6819` n `8`; equity avg `-0.155` n `88`; fx avg `0.0631` n `6`; index avg `-0.027` n `23`; metal avg `0.0714` n `20`; unknown avg `0.2528` n `743`
- 24h: commodity avg `-0.4335` n `12`; crypto_alt avg `-0.2248` n `228`; crypto_major avg `-0.4007` n `8`; equity avg `0.5969` n `88`; fx avg `0.1241` n `6`; index avg `0.0139` n `23`; metal avg `-0.6817` n `20`; unknown avg `0.1938` n `743`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
