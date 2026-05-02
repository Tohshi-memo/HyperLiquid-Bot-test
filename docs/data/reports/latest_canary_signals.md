# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T21:23:22.677720+00:00`
- Correlation status: `ready`
- Asset price records: `108`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `7`; crypto_alt avg `0.0653` n `223`; crypto_major avg `-0.0903` n `7`; equity avg `-0.0214` n `42`; fx avg `0.0019` n `4`; index avg `0.0045` n `9`; metal avg `0.0039` n `7`; unknown avg `0.0501` n `313`
- 1h: commodity avg `0.0531` n `7`; crypto_alt avg `0.0688` n `223`; crypto_major avg `0.0158` n `7`; equity avg `0.159` n `42`; fx avg `0.013` n `4`; index avg `0.0156` n `9`; metal avg `0.0063` n `7`; unknown avg `0.1595` n `313`
- 4h: commodity avg `-0.1147` n `7`; crypto_alt avg `0.3112` n `223`; crypto_major avg `-0.0161` n `7`; equity avg `0.5295` n `42`; fx avg `0.0183` n `4`; index avg `0.0567` n `9`; metal avg `-0.0484` n `7`; unknown avg `0.1736` n `313`
- 24h: commodity avg `-0.01` n `7`; crypto_alt avg `1.6921` n `223`; crypto_major avg `0.2059` n `7`; equity avg `1.1142` n `42`; fx avg `-0.0071` n `4`; index avg `0.0768` n `9`; metal avg `-0.0963` n `7`; unknown avg `0.3484` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5347`, n `100`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5311`, n `100`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.507`, n `104`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4895`, n `104`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4607`, n `100`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4245`, n `100`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4214`, n `100`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4197`, n `100`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4187`, n `104`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4183`, n `100`, moderate_sample_signal
