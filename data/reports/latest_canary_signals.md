# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T18:30:25.909087+00:00`
- Correlation status: `ready`
- Asset price records: `97`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `7`; crypto_alt avg `0.2703` n `223`; crypto_major avg `0.1421` n `7`; equity avg `0.0035` n `42`; fx avg `0.0` n `4`; index avg `0.0045` n `9`; metal avg `-0.0016` n `7`; unknown avg `0.0829` n `313`
- 1h: commodity avg `-0.0984` n `7`; crypto_alt avg `-0.0868` n `223`; crypto_major avg `-0.0463` n `7`; equity avg `0.1205` n `42`; fx avg `0.0011` n `4`; index avg `0.0214` n `9`; metal avg `-0.0407` n `7`; unknown avg `0.0218` n `313`
- 4h: commodity avg `-0.174` n `7`; crypto_alt avg `0.6062` n `223`; crypto_major avg `0.0914` n `7`; equity avg `0.2052` n `42`; fx avg `0.0823` n `4`; index avg `0.0325` n `9`; metal avg `-0.0277` n `7`; unknown avg `-0.0444` n `313`
- 24h: commodity avg `0.0294` n `7`; crypto_alt avg `1.1703` n `223`; crypto_major avg `0.1229` n `7`; equity avg `0.7207` n `42`; fx avg `-0.0287` n `4`; index avg `0.0841` n `9`; metal avg `-0.2772` n `7`; unknown avg `0.4046` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5329`, n `89`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5241`, n `93`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5075`, n `89`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5058`, n `93`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4697`, n `89`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4384`, n `89`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4295`, n `93`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4276`, n `89`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4257`, n `89`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4222`, n `89`, moderate_sample_signal
