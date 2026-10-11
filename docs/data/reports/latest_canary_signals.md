# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T10:37:28.322804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.006` n `13`; crypto_alt avg `-0.351` n `235`; crypto_major avg `-0.1523` n `8`; equity avg `-0.0191` n `150`; fx avg `-0.0056` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0531` n `1117`
- 1h: commodity avg `-0.0021` n `13`; crypto_alt avg `-0.45` n `235`; crypto_major avg `-0.1538` n `8`; equity avg `-0.0111` n `150`; fx avg `0.0048` n `6`; index avg `0.0017` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.4681` n `1115`
- 4h: commodity avg `0.0223` n `13`; crypto_alt avg `-0.3274` n `235`; crypto_major avg `-0.173` n `8`; equity avg `0.0523` n `150`; fx avg `-0.0005` n `6`; index avg `0.0084` n `26`; metal avg `0.005` n `20`; unknown avg `0.1456` n `1099`
- 24h: commodity avg `0.4365` n `13`; crypto_alt avg `0.8952` n `235`; crypto_major avg `-0.1008` n `8`; equity avg `0.0994` n `150`; fx avg `-0.0032` n `6`; index avg `-0.0048` n `26`; metal avg `0.0063` n `20`; unknown avg `0.6594` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
