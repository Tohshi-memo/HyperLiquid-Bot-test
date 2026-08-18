# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:08:18.798292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0169` n `12`; crypto_alt avg `-0.019` n `230`; crypto_major avg `-0.0218` n `8`; equity avg `-0.0957` n `120`; fx avg `0.0107` n `6`; index avg `0.0063` n `25`; metal avg `0.0029` n `20`; unknown avg `0.0213` n `789`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `0.0253` n `230`; crypto_major avg `0.1217` n `8`; equity avg `0.0885` n `120`; fx avg `0.0023` n `6`; index avg `0.0281` n `25`; metal avg `0.0221` n `20`; unknown avg `0.0515` n `789`
- 4h: commodity avg `0.1198` n `12`; crypto_alt avg `0.0017` n `230`; crypto_major avg `0.0308` n `8`; equity avg `-0.2005` n `120`; fx avg `-0.0026` n `6`; index avg `-0.0218` n `25`; metal avg `-0.0996` n `20`; unknown avg `3.6355` n `789`
- 24h: commodity avg `0.3549` n `12`; crypto_alt avg `-0.5073` n `230`; crypto_major avg `0.3387` n `8`; equity avg `-4.4438` n `120`; fx avg `-0.0453` n `6`; index avg `-0.6698` n `25`; metal avg `-0.6216` n `20`; unknown avg `-0.1612` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
