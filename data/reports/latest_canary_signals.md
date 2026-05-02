# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T20:27:36.074202+00:00`
- Correlation status: `ready`
- Asset price records: `104`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0351` n `7`; crypto_alt avg `-0.0303` n `223`; crypto_major avg `-0.0625` n `7`; equity avg `0.0648` n `42`; fx avg `0.0` n `4`; index avg `-0.0006` n `9`; metal avg `-0.0094` n `7`; unknown avg `0.026` n `313`
- 1h: commodity avg `-0.0566` n `7`; crypto_alt avg `0.0947` n `223`; crypto_major avg `-0.1668` n `7`; equity avg `0.1104` n `42`; fx avg `0.0074` n `4`; index avg `0.0044` n `9`; metal avg `-0.0006` n `7`; unknown avg `-0.0346` n `313`
- 4h: commodity avg `-0.2176` n `7`; crypto_alt avg `0.3813` n `223`; crypto_major avg `-0.0793` n `7`; equity avg `0.311` n `42`; fx avg `0.0412` n `4`; index avg `0.0457` n `9`; metal avg `-0.046` n `7`; unknown avg `0.1393` n `313`
- 24h: commodity avg `-0.0629` n `7`; crypto_alt avg `1.6114` n `223`; crypto_major avg `0.19` n `7`; equity avg `0.948` n `42`; fx avg `-0.0202` n `4`; index avg `0.0612` n `9`; metal avg `-0.1026` n `7`; unknown avg `0.1845` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5257`, n `96`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5101`, n `96`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5075`, n `100`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4899`, n `100`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4465`, n `96`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4294`, n `96`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4257`, n `96`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4179`, n `96`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4175`, n `100`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4167`, n `96`, moderate_sample_signal
