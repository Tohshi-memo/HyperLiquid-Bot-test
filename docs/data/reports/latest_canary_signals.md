# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T15:07:42.012348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `-0.0541` n `234`; crypto_major avg `-0.0087` n `8`; equity avg `-0.097` n `142`; fx avg `0.0398` n `6`; index avg `-0.035` n `26`; metal avg `-0.0932` n `20`; unknown avg `-0.0206` n `911`
- 1h: commodity avg `0.2082` n `12`; crypto_alt avg `-0.9484` n `234`; crypto_major avg `-0.8361` n `8`; equity avg `-0.2683` n `142`; fx avg `0.031` n `6`; index avg `-0.0522` n `26`; metal avg `-0.2035` n `20`; unknown avg `2.3656` n `911`
- 4h: commodity avg `0.1162` n `12`; crypto_alt avg `0.0565` n `234`; crypto_major avg `-0.3443` n `8`; equity avg `0.213` n `142`; fx avg `-0.0009` n `6`; index avg `0.1447` n `26`; metal avg `-0.1832` n `20`; unknown avg `7.7028` n `877`
- 24h: commodity avg `0.1019` n `12`; crypto_alt avg `-0.5571` n `234`; crypto_major avg `-0.411` n `8`; equity avg `-0.3954` n `142`; fx avg `0.0349` n `6`; index avg `0.1203` n `26`; metal avg `-0.0754` n `20`; unknown avg `12.4512` n `818`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
