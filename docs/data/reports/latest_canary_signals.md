# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T08:37:24.982717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.019` n `12`; crypto_alt avg `0.1715` n `230`; crypto_major avg `0.2415` n `8`; equity avg `0.0375` n `121`; fx avg `0.0026` n `6`; index avg `0.0027` n `25`; metal avg `-0.0059` n `20`; unknown avg `1.0523` n `794`
- 1h: commodity avg `-0.014` n `12`; crypto_alt avg `0.8158` n `230`; crypto_major avg `0.7898` n `8`; equity avg `0.1277` n `121`; fx avg `-0.0969` n `6`; index avg `0.0114` n `25`; metal avg `0.0016` n `20`; unknown avg `0.1087` n `794`
- 4h: commodity avg `-0.0006` n `12`; crypto_alt avg `1.4747` n `230`; crypto_major avg `0.5203` n `8`; equity avg `0.0004` n `121`; fx avg `-0.0457` n `6`; index avg `-0.0193` n `25`; metal avg `-0.0012` n `20`; unknown avg `0.5346` n `778`
- 24h: commodity avg `-0.0191` n `12`; crypto_alt avg `-1.7459` n `230`; crypto_major avg `0.0264` n `8`; equity avg `0.2132` n `121`; fx avg `0.0586` n `6`; index avg `0.0086` n `25`; metal avg `0.0669` n `20`; unknown avg `2.6127` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
