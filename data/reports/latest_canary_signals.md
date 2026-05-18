# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T06:37:14.498596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `0.1098` n `228`; crypto_major avg `0.1246` n `8`; equity avg `0.067` n `66`; fx avg `0.008` n `5`; index avg `-0.0161` n `23`; metal avg `0.0491` n `18`; unknown avg `-0.1054` n `383`
- 1h: commodity avg `0.2057` n `12`; crypto_alt avg `-0.5551` n `228`; crypto_major avg `-0.6475` n `8`; equity avg `-0.1339` n `66`; fx avg `-0.0229` n `5`; index avg `-0.1238` n `23`; metal avg `-0.1089` n `18`; unknown avg `0.0099` n `363`
- 4h: commodity avg `0.11` n `12`; crypto_alt avg `-0.7145` n `228`; crypto_major avg `-0.6447` n `8`; equity avg `-0.3541` n `66`; fx avg `-0.0313` n `5`; index avg `-0.0529` n `23`; metal avg `0.069` n `18`; unknown avg `-0.2499` n `363`
- 24h: commodity avg `2.8129` n `12`; crypto_alt avg `-11.4153` n `228`; crypto_major avg `-3.908` n `8`; equity avg `-3.11` n `65`; fx avg `-0.1117` n `5`; index avg `-1.806` n `23`; metal avg `-6.1223` n `18`; unknown avg `-1.1519` n `357`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
