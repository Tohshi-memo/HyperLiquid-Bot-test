# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T15:37:23.121630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `0.2086` n `228`; crypto_major avg `0.2996` n `8`; equity avg `0.0887` n `74`; fx avg `0.0013` n `6`; index avg `0.128` n `23`; metal avg `0.0325` n `18`; unknown avg `0.0422` n `516`
- 1h: commodity avg `0.1418` n `12`; crypto_alt avg `-0.3468` n `228`; crypto_major avg `-0.196` n `8`; equity avg `-0.1396` n `74`; fx avg `0.002` n `6`; index avg `-0.0785` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.0279` n `516`
- 4h: commodity avg `0.2604` n `12`; crypto_alt avg `-0.2804` n `228`; crypto_major avg `-0.2489` n `8`; equity avg `0.3171` n `74`; fx avg `0.011` n `6`; index avg `0.2375` n `23`; metal avg `-0.1152` n `18`; unknown avg `0.1709` n `516`
- 24h: commodity avg `0.2593` n `12`; crypto_alt avg `2.6456` n `228`; crypto_major avg `2.8305` n `8`; equity avg `1.987` n `74`; fx avg `0.031` n `6`; index avg `0.4057` n `23`; metal avg `0.661` n `18`; unknown avg `-4.6228` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
