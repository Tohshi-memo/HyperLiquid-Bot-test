# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T13:52:33.298542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1072` n `12`; crypto_alt avg `0.4795` n `228`; crypto_major avg `0.6755` n `8`; equity avg `0.2023` n `86`; fx avg `-0.0069` n `6`; index avg `-0.0154` n `23`; metal avg `0.162` n `20`; unknown avg `0.1006` n `765`
- 1h: commodity avg `-0.0624` n `12`; crypto_alt avg `0.7031` n `228`; crypto_major avg `0.769` n `8`; equity avg `0.4476` n `86`; fx avg `-0.0007` n `6`; index avg `-0.0139` n `23`; metal avg `0.0769` n `20`; unknown avg `0.1391` n `765`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `-0.069` n `228`; crypto_major avg `-0.1147` n `8`; equity avg `0.0317` n `86`; fx avg `0.0121` n `6`; index avg `-0.076` n `23`; metal avg `0.1277` n `20`; unknown avg `-0.0966` n `765`
- 24h: commodity avg `-0.185` n `12`; crypto_alt avg `1.5605` n `228`; crypto_major avg `1.5606` n `8`; equity avg `-1.2986` n `86`; fx avg `0.0422` n `6`; index avg `-0.3777` n `23`; metal avg `0.689` n `20`; unknown avg `1.1742` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3417`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
