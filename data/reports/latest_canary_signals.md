# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T15:37:17.480096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.2533` n `228`; crypto_major avg `-0.3512` n `8`; equity avg `-0.0791` n `67`; fx avg `-0.0061` n `6`; index avg `-0.0964` n `23`; metal avg `-0.0975` n `18`; unknown avg `0.0608` n `418`
- 1h: commodity avg `0.2807` n `12`; crypto_alt avg `-1.1466` n `228`; crypto_major avg `-1.0362` n `8`; equity avg `-0.267` n `67`; fx avg `-0.0031` n `6`; index avg `-0.2318` n `23`; metal avg `-0.4068` n `18`; unknown avg `0.7665` n `418`
- 4h: commodity avg `0.8743` n `12`; crypto_alt avg `-0.7584` n `228`; crypto_major avg `-0.5359` n `8`; equity avg `-0.0909` n `67`; fx avg `-0.0314` n `6`; index avg `0.1983` n `23`; metal avg `-0.31` n `18`; unknown avg `-0.3494` n `415`
- 24h: commodity avg `1.2367` n `12`; crypto_alt avg `-1.038` n `228`; crypto_major avg `-1.1349` n `8`; equity avg `-0.5086` n `67`; fx avg `-0.1722` n `6`; index avg `0.2835` n `23`; metal avg `-1.2358` n `18`; unknown avg `-0.5819` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
