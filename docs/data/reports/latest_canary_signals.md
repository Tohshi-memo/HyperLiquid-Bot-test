# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T03:22:35.300574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.127` n `233`; crypto_major avg `0.1009` n `8`; equity avg `-0.0987` n `136`; fx avg `-0.0093` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0406` n `20`; unknown avg `0.4571` n `796`
- 1h: commodity avg `0.0787` n `12`; crypto_alt avg `-0.1209` n `233`; crypto_major avg `-0.1685` n `8`; equity avg `-0.3774` n `136`; fx avg `-0.031` n `6`; index avg `-0.0502` n `26`; metal avg `-0.0983` n `20`; unknown avg `-0.5708` n `794`
- 4h: commodity avg `-0.1151` n `12`; crypto_alt avg `0.0165` n `233`; crypto_major avg `-0.0392` n `8`; equity avg `-0.2479` n `136`; fx avg `-0.061` n `6`; index avg `0.0029` n `26`; metal avg `-0.0914` n `20`; unknown avg `-0.5296` n `778`
- 24h: commodity avg `1.2112` n `12`; crypto_alt avg `-2.4697` n `233`; crypto_major avg `-2.7003` n `8`; equity avg `-2.1314` n `136`; fx avg `0.064` n `6`; index avg `-0.3549` n `26`; metal avg `-1.3687` n `20`; unknown avg `-0.9156` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
