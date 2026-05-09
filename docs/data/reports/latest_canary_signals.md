# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T15:52:16.757141+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0184` n `228`; crypto_major avg `-0.0321` n `8`; equity avg `-0.0449` n `65`; fx avg `0.0` n `5`; index avg `0.0084` n `23`; metal avg `0.019` n `18`; unknown avg `-0.016` n `376`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `-0.0683` n `228`; crypto_major avg `0.1119` n `8`; equity avg `0.0032` n `65`; fx avg `-0.0138` n `5`; index avg `0.0536` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.0156` n `376`
- 4h: commodity avg `0.392` n `12`; crypto_alt avg `-1.0823` n `228`; crypto_major avg `-0.4782` n `8`; equity avg `0.0177` n `65`; fx avg `-0.007` n `5`; index avg `0.0512` n `23`; metal avg `-0.0645` n `18`; unknown avg `-0.1876` n `376`
- 24h: commodity avg `-0.3293` n `12`; crypto_alt avg `1.3142` n `228`; crypto_major avg `1.1784` n `8`; equity avg `1.7585` n `65`; fx avg `0.0071` n `5`; index avg `0.6915` n `23`; metal avg `0.1767` n `18`; unknown avg `0.2414` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
