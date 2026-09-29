# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T02:52:40.559668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0896` n `12`; crypto_alt avg `-0.0293` n `234`; crypto_major avg `0.0115` n `8`; equity avg `-0.11` n `141`; fx avg `0.023` n `6`; index avg `-0.0361` n `26`; metal avg `0.0116` n `20`; unknown avg `0.3818` n `963`
- 1h: commodity avg `0.0468` n `12`; crypto_alt avg `-0.8174` n `234`; crypto_major avg `-0.2179` n `8`; equity avg `-0.251` n `141`; fx avg `-0.0102` n `6`; index avg `-0.0618` n `26`; metal avg `0.0034` n `20`; unknown avg `-0.19` n `961`
- 4h: commodity avg `0.1046` n `12`; crypto_alt avg `-1.8753` n `234`; crypto_major avg `-1.0839` n `8`; equity avg `-0.4902` n `141`; fx avg `-0.0292` n `6`; index avg `-0.0978` n `26`; metal avg `-0.0162` n `20`; unknown avg `0.6835` n `955`
- 24h: commodity avg `0.1924` n `12`; crypto_alt avg `-4.2362` n `234`; crypto_major avg `-1.8476` n `8`; equity avg `-2.2089` n `141`; fx avg `-0.0425` n `6`; index avg `-0.2191` n `26`; metal avg `-0.4449` n `20`; unknown avg `10.1364` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
