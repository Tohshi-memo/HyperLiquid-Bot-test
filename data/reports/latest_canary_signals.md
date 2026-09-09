# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T08:23:06.425571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `12`; crypto_alt avg `0.1169` n `233`; crypto_major avg `0.0009` n `8`; equity avg `0.0589` n `134`; fx avg `0.0012` n `6`; index avg `-0.0084` n `26`; metal avg `-0.0663` n `20`; unknown avg `0.0843` n `798`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.3092` n `233`; crypto_major avg `0.1355` n `8`; equity avg `0.1496` n `134`; fx avg `-0.0125` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0518` n `20`; unknown avg `0.1002` n `796`
- 4h: commodity avg `0.0927` n `12`; crypto_alt avg `1.2577` n `233`; crypto_major avg `0.7754` n `8`; equity avg `0.4006` n `134`; fx avg `0.0157` n `6`; index avg `0.0244` n `26`; metal avg `0.2277` n `20`; unknown avg `1.1295` n `772`
- 24h: commodity avg `-0.2316` n `12`; crypto_alt avg `1.3455` n `232`; crypto_major avg `1.8954` n `8`; equity avg `1.7927` n `134`; fx avg `-0.0966` n `6`; index avg `0.1208` n `26`; metal avg `0.093` n `20`; unknown avg `0.9994` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
