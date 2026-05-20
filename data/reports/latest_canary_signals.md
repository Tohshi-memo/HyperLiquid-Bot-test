# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T00:52:13.413430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `-0.023` n `228`; crypto_major avg `0.0486` n `8`; equity avg `-0.0389` n `66`; fx avg `-0.0121` n `6`; index avg `-0.0652` n `23`; metal avg `0.0159` n `18`; unknown avg `-0.1545` n `384`
- 1h: commodity avg `-0.1077` n `12`; crypto_alt avg `-0.1311` n `228`; crypto_major avg `-0.3499` n `8`; equity avg `-0.333` n `66`; fx avg `0.0224` n `6`; index avg `-0.2654` n `23`; metal avg `0.108` n `18`; unknown avg `-0.31` n `383`
- 4h: commodity avg `-0.1838` n `12`; crypto_alt avg `-0.4641` n `228`; crypto_major avg `-0.4459` n `8`; equity avg `-0.2045` n `66`; fx avg `0.0087` n `6`; index avg `-0.0664` n `23`; metal avg `0.4656` n `18`; unknown avg `-0.4611` n `383`
- 24h: commodity avg `0.9007` n `12`; crypto_alt avg `-1.7331` n `228`; crypto_major avg `-1.4142` n `8`; equity avg `-0.5543` n `66`; fx avg `-0.0154` n `6`; index avg `-0.7657` n `23`; metal avg `-2.4084` n `18`; unknown avg `0.5184` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0465`, n `668`, weak_sample_signal
