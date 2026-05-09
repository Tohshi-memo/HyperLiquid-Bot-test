# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T15:40:48.369770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1031` n `12`; crypto_alt avg `-0.0219` n `228`; crypto_major avg `0.1617` n `8`; equity avg `0.0336` n `65`; fx avg `-0.0236` n `5`; index avg `0.0103` n `23`; metal avg `0.015` n `18`; unknown avg `0.0442` n `376`
- 1h: commodity avg `0.0915` n `12`; crypto_alt avg `-0.0319` n `228`; crypto_major avg `0.0926` n `8`; equity avg `0.0877` n `65`; fx avg `-0.0117` n `5`; index avg `0.0473` n `23`; metal avg `-0.0314` n `18`; unknown avg `0.1272` n `376`
- 4h: commodity avg `0.3768` n `12`; crypto_alt avg `-1.1766` n `228`; crypto_major avg `-0.4432` n `8`; equity avg `0.0668` n `65`; fx avg `-0.0204` n `5`; index avg `0.0437` n `23`; metal avg `-0.0791` n `18`; unknown avg `-0.0788` n `376`
- 24h: commodity avg `-0.1702` n `12`; crypto_alt avg `1.6412` n `228`; crypto_major avg `1.5579` n `8`; equity avg `1.6189` n `65`; fx avg `0.0238` n `5`; index avg `0.6239` n `23`; metal avg `0.1021` n `18`; unknown avg `0.3693` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
