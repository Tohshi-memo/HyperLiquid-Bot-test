# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T13:37:29.528437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0226` n `12`; crypto_alt avg `0.0969` n `234`; crypto_major avg `0.0653` n `8`; equity avg `0.0143` n `141`; fx avg `-0.003` n `6`; index avg `0.0013` n `26`; metal avg `0.0068` n `20`; unknown avg `0.0648` n `962`
- 1h: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.7458` n `234`; crypto_major avg `-0.581` n `8`; equity avg `-0.0376` n `141`; fx avg `-0.0008` n `6`; index avg `0.0` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.3811` n `960`
- 4h: commodity avg `-0.0058` n `12`; crypto_alt avg `-0.7342` n `234`; crypto_major avg `-0.2561` n `8`; equity avg `-0.0189` n `141`; fx avg `-0.005` n `6`; index avg `-0.0156` n `26`; metal avg `-0.0116` n `20`; unknown avg `2.354` n `953`
- 24h: commodity avg `0.0242` n `12`; crypto_alt avg `0.4388` n `234`; crypto_major avg `0.6763` n `8`; equity avg `0.3459` n `141`; fx avg `-0.0303` n `6`; index avg `0.0307` n `26`; metal avg `-0.0136` n `20`; unknown avg `73.7272` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
