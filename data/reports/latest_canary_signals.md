# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T22:07:30.076037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `13`; crypto_alt avg `0.0715` n `239`; crypto_major avg `0.1021` n `8`; equity avg `0.1512` n `168`; fx avg `-0.0082` n `6`; index avg `0.0178` n `27`; metal avg `0.024` n `20`; unknown avg `-0.0009` n `1249`
- 1h: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0173` n `239`; crypto_major avg `0.2964` n `8`; equity avg `0.229` n `168`; fx avg `-0.0164` n `6`; index avg `0.0181` n `27`; metal avg `0.0573` n `20`; unknown avg `22.6572` n `1249`
- 4h: commodity avg `0.0237` n `13`; crypto_alt avg `-0.7953` n `239`; crypto_major avg `-0.2639` n `8`; equity avg `0.0603` n `168`; fx avg `-0.0589` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0331` n `20`; unknown avg `397.7254` n `1201`
- 24h: commodity avg `0.6339` n `13`; crypto_alt avg `-2.7324` n `239`; crypto_major avg `-2.4164` n `8`; equity avg `-4.0585` n `167`; fx avg `0.2263` n `6`; index avg `-0.2759` n `27`; metal avg `-1.048` n `20`; unknown avg `426.4679` n `1111`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
