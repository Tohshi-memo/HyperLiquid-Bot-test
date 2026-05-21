# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T05:22:17.608615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `-0.2659` n `228`; crypto_major avg `-0.159` n `8`; equity avg `-0.0035` n `66`; fx avg `0.0179` n `6`; index avg `0.0256` n `23`; metal avg `-0.2025` n `18`; unknown avg `1.2711` n `384`
- 1h: commodity avg `-0.124` n `12`; crypto_alt avg `-0.2068` n `228`; crypto_major avg `-0.1966` n `8`; equity avg `0.2151` n `66`; fx avg `0.0098` n `6`; index avg `0.067` n `23`; metal avg `-0.2023` n `18`; unknown avg `-0.5829` n `384`
- 4h: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0031` n `228`; crypto_major avg `-0.0406` n `8`; equity avg `0.3683` n `66`; fx avg `0.0449` n `6`; index avg `0.2598` n `23`; metal avg `-0.955` n `18`; unknown avg `-0.0338` n `384`
- 24h: commodity avg `-2.2762` n `12`; crypto_alt avg `2.8203` n `228`; crypto_major avg `3.2619` n `8`; equity avg `2.7154` n `66`; fx avg `0.0365` n `6`; index avg `1.7962` n `23`; metal avg `1.0621` n `18`; unknown avg `4.5287` n `374`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
