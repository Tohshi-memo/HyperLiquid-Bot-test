# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T05:37:27.902174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1292` n `12`; crypto_alt avg `-0.0112` n `233`; crypto_major avg `0.086` n `8`; equity avg `0.0811` n `136`; fx avg `0.0043` n `6`; index avg `0.0025` n `26`; metal avg `0.0643` n `20`; unknown avg `0.4096` n `796`
- 1h: commodity avg `-0.2493` n `12`; crypto_alt avg `-0.1359` n `233`; crypto_major avg `0.0885` n `8`; equity avg `0.1423` n `136`; fx avg `0.0253` n `6`; index avg `0.0058` n `26`; metal avg `0.1292` n `20`; unknown avg `7.2707` n `794`
- 4h: commodity avg `-0.2138` n `12`; crypto_alt avg `0.5789` n `233`; crypto_major avg `0.614` n `8`; equity avg `0.0156` n `136`; fx avg `-0.0483` n `6`; index avg `0.0654` n `26`; metal avg `0.1545` n `20`; unknown avg `11.7064` n `780`
- 24h: commodity avg `0.9319` n `12`; crypto_alt avg `-1.8336` n `233`; crypto_major avg `-2.0228` n `8`; equity avg `-1.9989` n `136`; fx avg `0.077` n `6`; index avg `-0.3439` n `26`; metal avg `-1.1885` n `20`; unknown avg `-0.403` n `675`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
