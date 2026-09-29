# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T09:52:45.994957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `12`; crypto_alt avg `0.1732` n `234`; crypto_major avg `0.2161` n `8`; equity avg `0.0881` n `141`; fx avg `0.0081` n `6`; index avg `0.0106` n `26`; metal avg `0.0106` n `20`; unknown avg `0.0662` n `963`
- 1h: commodity avg `-0.102` n `12`; crypto_alt avg `0.503` n `234`; crypto_major avg `0.4832` n `8`; equity avg `-0.0551` n `141`; fx avg `-0.0053` n `6`; index avg `-0.0241` n `26`; metal avg `0.0275` n `20`; unknown avg `0.1822` n `961`
- 4h: commodity avg `-0.4357` n `12`; crypto_alt avg `2.0425` n `234`; crypto_major avg `1.2502` n `8`; equity avg `0.9464` n `141`; fx avg `-0.0273` n `6`; index avg `0.1221` n `26`; metal avg `0.0613` n `20`; unknown avg `1.0956` n `927`
- 24h: commodity avg `-0.623` n `12`; crypto_alt avg `2.1873` n `234`; crypto_major avg `1.5073` n `8`; equity avg `-0.1232` n `141`; fx avg `-0.0673` n `6`; index avg `-0.0512` n `26`; metal avg `-0.2177` n `20`; unknown avg `45.0752` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
