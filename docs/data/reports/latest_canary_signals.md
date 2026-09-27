# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T10:07:28.428872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.034` n `234`; crypto_major avg `-0.0131` n `8`; equity avg `-0.0062` n `141`; fx avg `-0.0073` n `6`; index avg `0.0022` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.2863` n `960`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.3263` n `234`; crypto_major avg `0.3445` n `8`; equity avg `0.0341` n `141`; fx avg `-0.0021` n `6`; index avg `0.0027` n `26`; metal avg `0.0134` n `20`; unknown avg `0.2831` n `959`
- 4h: commodity avg `-0.0211` n `12`; crypto_alt avg `0.8833` n `234`; crypto_major avg `0.8155` n `8`; equity avg `0.1749` n `141`; fx avg `-0.0224` n `6`; index avg `0.0332` n `26`; metal avg `0.0168` n `20`; unknown avg `2.0957` n `943`
- 24h: commodity avg `0.0483` n `12`; crypto_alt avg `1.2801` n `234`; crypto_major avg `1.0279` n `8`; equity avg `0.4251` n `141`; fx avg `-0.0097` n `6`; index avg `0.0368` n `26`; metal avg `0.008` n `20`; unknown avg `5.474` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
