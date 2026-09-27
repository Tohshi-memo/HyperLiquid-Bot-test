# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T07:12:20.048598+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `0.2306` n `234`; crypto_major avg `0.0001` n `8`; equity avg `0.0008` n `141`; fx avg `-0.0045` n `6`; index avg `-0.0002` n `26`; metal avg `0.0082` n `20`; unknown avg `2.0628` n `959`
- 1h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.4288` n `234`; crypto_major avg `0.0296` n `8`; equity avg `0.0352` n `141`; fx avg `-0.0074` n `6`; index avg `0.0051` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.0326` n `959`
- 4h: commodity avg `0.0145` n `12`; crypto_alt avg `0.6898` n `234`; crypto_major avg `0.0677` n `8`; equity avg `0.0488` n `141`; fx avg `0.0074` n `6`; index avg `0.0147` n `26`; metal avg `-0.0033` n `20`; unknown avg `24.468` n `933`
- 24h: commodity avg `0.06` n `12`; crypto_alt avg `0.9197` n `234`; crypto_major avg `0.064` n `8`; equity avg `0.2858` n `141`; fx avg `0.0158` n `6`; index avg `0.0073` n `26`; metal avg `-0.0097` n `20`; unknown avg `4.7793` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
