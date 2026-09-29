# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T03:52:28.427316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.0952` n `234`; crypto_major avg `-0.0468` n `8`; equity avg `-0.0494` n `141`; fx avg `-0.0011` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0155` n `20`; unknown avg `1.8224` n `963`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `1.0884` n `234`; crypto_major avg `0.6781` n `8`; equity avg `0.0354` n `141`; fx avg `-0.0193` n `6`; index avg `0.0113` n `26`; metal avg `-0.012` n `20`; unknown avg `2.2573` n `961`
- 4h: commodity avg `0.1308` n `12`; crypto_alt avg `-1.5231` n `234`; crypto_major avg `-0.6241` n `8`; equity avg `-0.4421` n `141`; fx avg `-0.0306` n `6`; index avg `-0.0743` n `26`; metal avg `-0.0443` n `20`; unknown avg `1.1726` n `955`
- 24h: commodity avg `0.1291` n `12`; crypto_alt avg `-2.581` n `234`; crypto_major avg `-1.0139` n `8`; equity avg `-2.0894` n `141`; fx avg `-0.0518` n `6`; index avg `-0.2064` n `26`; metal avg `-0.479` n `20`; unknown avg `9.8325` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
