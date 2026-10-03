# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T04:22:37.177590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.19` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `-0.2159` n `235`; crypto_major avg `-0.2238` n `8`; equity avg `-0.032` n `143`; fx avg `0.003` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.0095` n `984`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.2832` n `235`; crypto_major avg `-0.1158` n `8`; equity avg `-0.053` n `143`; fx avg `0.0053` n `6`; index avg `-0.0041` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.2043` n `976`
- 4h: commodity avg `-0.212` n `13`; crypto_alt avg `-0.0635` n `235`; crypto_major avg `-0.2531` n `8`; equity avg `-0.076` n `143`; fx avg `0.0156` n `6`; index avg `0.0157` n `26`; metal avg `-0.0144` n `20`; unknown avg `-0.2858` n `976`
- 24h: commodity avg `0.0868` n `13`; crypto_alt avg `-1.1008` n `235`; crypto_major avg `-1.6794` n `8`; equity avg `0.5036` n `142`; fx avg `-0.1144` n `6`; index avg `0.2514` n `26`; metal avg `-0.3351` n `20`; unknown avg `-0.8517` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1733`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
