# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T08:22:30.490721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.2611` n `228`; crypto_major avg `0.1526` n `8`; equity avg `0.0683` n `74`; fx avg `0.0037` n `6`; index avg `0.0375` n `23`; metal avg `0.0127` n `18`; unknown avg `55.5575` n `645`
- 1h: commodity avg `-0.1691` n `12`; crypto_alt avg `0.1513` n `228`; crypto_major avg `-0.0626` n `8`; equity avg `0.2012` n `74`; fx avg `-0.0019` n `6`; index avg `0.0577` n `23`; metal avg `0.0376` n `18`; unknown avg `55.5716` n `645`
- 4h: commodity avg `-0.293` n `12`; crypto_alt avg `-0.235` n `228`; crypto_major avg `-0.3791` n `8`; equity avg `0.1926` n `74`; fx avg `0.002` n `6`; index avg `0.0185` n `23`; metal avg `0.0339` n `18`; unknown avg `2.8601` n `625`
- 24h: commodity avg `-0.9246` n `12`; crypto_alt avg `0.5291` n `228`; crypto_major avg `0.7825` n `8`; equity avg `0.7813` n `74`; fx avg `-0.0178` n `6`; index avg `0.2858` n `23`; metal avg `0.2483` n `18`; unknown avg `-0.5457` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
