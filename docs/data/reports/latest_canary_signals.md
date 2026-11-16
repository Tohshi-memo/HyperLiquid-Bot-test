# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T13:22:26.990517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0376` n `13`; crypto_alt avg `-0.2249` n `239`; crypto_major avg `-0.2499` n `8`; equity avg `-0.314` n `162`; fx avg `0.0138` n `6`; index avg `-0.0409` n `27`; metal avg `-0.0757` n `20`; unknown avg `234.1782` n `1263`
- 1h: commodity avg `-0.0793` n `13`; crypto_alt avg `-0.3145` n `239`; crypto_major avg `-0.1613` n `8`; equity avg `-0.0293` n `162`; fx avg `0.0264` n `6`; index avg `0.035` n `27`; metal avg `-0.0493` n `20`; unknown avg `0.2739` n `1261`
- 4h: commodity avg `-0.0793` n `13`; crypto_alt avg `-0.6597` n `239`; crypto_major avg `-0.233` n `8`; equity avg `-0.8592` n `162`; fx avg `0.0117` n `6`; index avg `-0.1004` n `27`; metal avg `0.0033` n `20`; unknown avg `-0.2132` n `1255`
- 24h: commodity avg `-0.5818` n `13`; crypto_alt avg `-2.4861` n `239`; crypto_major avg `-2.4611` n `8`; equity avg `-1.7818` n `162`; fx avg `-0.006` n `6`; index avg `-0.1424` n `27`; metal avg `-0.0142` n `20`; unknown avg `304.6232` n `1054`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
