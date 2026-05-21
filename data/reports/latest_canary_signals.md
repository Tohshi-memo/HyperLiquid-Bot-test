# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T00:52:16.343482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `12`; crypto_alt avg `0.2587` n `228`; crypto_major avg `0.3336` n `8`; equity avg `0.2033` n `66`; fx avg `-0.0025` n `6`; index avg `0.0876` n `23`; metal avg `0.0747` n `18`; unknown avg `0.1736` n `384`
- 1h: commodity avg `0.1388` n `12`; crypto_alt avg `0.7857` n `228`; crypto_major avg `0.7586` n `8`; equity avg `0.4924` n `66`; fx avg `-0.0026` n `6`; index avg `0.1726` n `23`; metal avg `0.0016` n `18`; unknown avg `0.3354` n `384`
- 4h: commodity avg `0.0182` n `12`; crypto_alt avg `0.487` n `228`; crypto_major avg `1.3097` n `8`; equity avg `0.2404` n `66`; fx avg `0.0313` n `6`; index avg `0.0777` n `23`; metal avg `0.0114` n `18`; unknown avg `2.7185` n `384`
- 24h: commodity avg `-2.1253` n `12`; crypto_alt avg `3.7775` n `228`; crypto_major avg `3.6642` n `8`; equity avg `2.2024` n `66`; fx avg `-0.06` n `6`; index avg `1.31` n `23`; metal avg `1.1235` n `18`; unknown avg `4.2102` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0451`, n `668`, weak_sample_signal
