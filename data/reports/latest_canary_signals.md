# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T03:37:28.096080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.1661` n `228`; crypto_major avg `-0.1657` n `8`; equity avg `0.0318` n `78`; fx avg `0.0` n `6`; index avg `-0.0061` n `23`; metal avg `0.008` n `18`; unknown avg `-0.1938` n `702`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.0703` n `228`; crypto_major avg `0.1103` n `8`; equity avg `0.0635` n `78`; fx avg `0.0007` n `6`; index avg `0.0104` n `23`; metal avg `0.0204` n `18`; unknown avg `-0.3712` n `702`
- 4h: commodity avg `0.0147` n `12`; crypto_alt avg `0.1673` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `0.1029` n `78`; fx avg `-0.0083` n `6`; index avg `0.0043` n `23`; metal avg `0.0085` n `18`; unknown avg `1.0999` n `701`
- 24h: commodity avg `0.1824` n `12`; crypto_alt avg `1.6401` n `228`; crypto_major avg `1.6546` n `8`; equity avg `0.4629` n `78`; fx avg `0.0325` n `6`; index avg `0.0072` n `23`; metal avg `0.0299` n `18`; unknown avg `1.8211` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
