# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T03:37:28.590507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `12`; crypto_alt avg `0.3249` n `234`; crypto_major avg `0.2341` n `8`; equity avg `0.0658` n `141`; fx avg `-0.0071` n `6`; index avg `0.0055` n `26`; metal avg `-0.0167` n `20`; unknown avg `0.625` n `963`
- 1h: commodity avg `0.0722` n `12`; crypto_alt avg `1.1559` n `234`; crypto_major avg `0.737` n `8`; equity avg `-0.0255` n `141`; fx avg `0.0048` n `6`; index avg `-0.0162` n `26`; metal avg `0.015` n `20`; unknown avg `0.8803` n `961`
- 4h: commodity avg `0.1231` n `12`; crypto_alt avg `-1.3025` n `234`; crypto_major avg `-0.566` n `8`; equity avg `-0.4666` n `141`; fx avg `-0.0106` n `6`; index avg `-0.0826` n `26`; metal avg `-0.0445` n `20`; unknown avg `1.2306` n `955`
- 24h: commodity avg `0.1459` n `12`; crypto_alt avg `-2.2961` n `234`; crypto_major avg `-0.9417` n `8`; equity avg `-1.9261` n `141`; fx avg `-0.0604` n `6`; index avg `-0.1772` n `26`; metal avg `-0.4293` n `20`; unknown avg `9.8991` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
