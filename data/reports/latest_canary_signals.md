# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T11:37:30.716725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0399` n `12`; crypto_alt avg `0.1388` n `234`; crypto_major avg `0.1253` n `8`; equity avg `0.1305` n `142`; fx avg `-0.0014` n `6`; index avg `0.0437` n `26`; metal avg `0.0737` n `20`; unknown avg `2.3468` n `963`
- 1h: commodity avg `0.0995` n `12`; crypto_alt avg `-0.1722` n `234`; crypto_major avg `0.0398` n `8`; equity avg `-0.0665` n `142`; fx avg `0.0001` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0402` n `20`; unknown avg `3.7818` n `961`
- 4h: commodity avg `0.3961` n `12`; crypto_alt avg `0.7274` n `234`; crypto_major avg `0.846` n `8`; equity avg `-0.2669` n `142`; fx avg `0.1048` n `6`; index avg `-0.0787` n `26`; metal avg `-0.1805` n `20`; unknown avg `2.0459` n `945`
- 24h: commodity avg `-0.2029` n `12`; crypto_alt avg `-0.281` n `234`; crypto_major avg `-0.3639` n `8`; equity avg `-0.157` n `142`; fx avg `0.0418` n `6`; index avg `-0.023` n `26`; metal avg `0.0233` n `20`; unknown avg `2924.0357` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
