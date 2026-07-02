# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T03:52:26.262196+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0235` n `12`; crypto_alt avg `0.4222` n `228`; crypto_major avg `0.5859` n `8`; equity avg `-0.0608` n `88`; fx avg `-0.008` n `6`; index avg `-0.0285` n `25`; metal avg `0.0948` n `20`; unknown avg `-0.0281` n `761`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.5225` n `228`; crypto_major avg `0.8645` n `8`; equity avg `-0.2096` n `88`; fx avg `-0.0072` n `6`; index avg `-0.0618` n `25`; metal avg `0.148` n `20`; unknown avg `-0.1377` n `761`
- 4h: commodity avg `-0.0881` n `12`; crypto_alt avg `1.4866` n `228`; crypto_major avg `1.4831` n `8`; equity avg `0.0917` n `88`; fx avg `0.0011` n `6`; index avg `0.0649` n `25`; metal avg `0.5549` n `20`; unknown avg `-0.1828` n `759`
- 24h: commodity avg `-0.6722` n `12`; crypto_alt avg `1.8748` n `228`; crypto_major avg `1.4393` n `8`; equity avg `-1.5075` n `88`; fx avg `-0.0488` n `6`; index avg `-0.3973` n `25`; metal avg `1.1822` n `20`; unknown avg `25.2947` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
