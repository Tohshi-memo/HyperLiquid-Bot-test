# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T15:37:12.376391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0487` n `12`; crypto_alt avg `0.032` n `228`; crypto_major avg `0.1633` n `8`; equity avg `0.0355` n `65`; fx avg `-0.0236` n `5`; index avg `-0.0004` n `23`; metal avg `0.0034` n `18`; unknown avg `0.1042` n `376`
- 1h: commodity avg `0.1461` n `12`; crypto_alt avg `0.0225` n `228`; crypto_major avg `0.0942` n `8`; equity avg `0.0896` n `65`; fx avg `-0.0117` n `5`; index avg `0.0367` n `23`; metal avg `-0.0429` n `18`; unknown avg `0.1854` n `376`
- 4h: commodity avg `0.4317` n `12`; crypto_alt avg `-1.1234` n `228`; crypto_major avg `-0.4417` n `8`; equity avg `0.0687` n `65`; fx avg `-0.0204` n `5`; index avg `0.0331` n `23`; metal avg `-0.0907` n `18`; unknown avg `-0.0022` n `376`
- 24h: commodity avg `-0.1158` n `12`; crypto_alt avg `1.698` n `228`; crypto_major avg `1.5596` n `8`; equity avg `1.6207` n `65`; fx avg `0.0238` n `5`; index avg `0.6132` n `23`; metal avg `0.0904` n `18`; unknown avg `0.3938` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
