# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T03:52:32.621957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0666` n `12`; crypto_alt avg `0.0101` n `233`; crypto_major avg `-0.0556` n `8`; equity avg `-0.0` n `136`; fx avg `-0.0063` n `6`; index avg `0.0102` n `26`; metal avg `-0.0478` n `20`; unknown avg `1.2024` n `796`
- 1h: commodity avg `0.1259` n `12`; crypto_alt avg `0.1206` n `233`; crypto_major avg `-0.0677` n `8`; equity avg `-0.176` n `136`; fx avg `-0.0083` n `6`; index avg `-0.0121` n `26`; metal avg `-0.1067` n `20`; unknown avg `0.8498` n `792`
- 4h: commodity avg `-0.2045` n `12`; crypto_alt avg `0.3121` n `233`; crypto_major avg `0.1518` n `8`; equity avg `-0.1533` n `136`; fx avg `-0.0804` n `6`; index avg `0.0381` n `26`; metal avg `-0.0656` n `20`; unknown avg `-0.5061` n `776`
- 24h: commodity avg `1.2498` n `12`; crypto_alt avg `-2.2013` n `233`; crypto_major avg `-2.4891` n `8`; equity avg `-2.1319` n `136`; fx avg `0.091` n `6`; index avg `-0.3608` n `26`; metal avg `-1.3533` n `20`; unknown avg `-1.0326` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
