# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T03:52:16.748394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `12`; crypto_alt avg `-0.1645` n `228`; crypto_major avg `-0.1406` n `8`; equity avg `-0.0994` n `66`; fx avg `0.0064` n `6`; index avg `-0.0645` n `23`; metal avg `-0.1179` n `18`; unknown avg `-0.0499` n `384`
- 1h: commodity avg `-0.067` n `12`; crypto_alt avg `0.1338` n `228`; crypto_major avg `0.0757` n `8`; equity avg `0.0233` n `66`; fx avg `0.0384` n `6`; index avg `-0.0657` n `23`; metal avg `0.1109` n `18`; unknown avg `17.3941` n `384`
- 4h: commodity avg `-0.1575` n `12`; crypto_alt avg `0.0782` n `228`; crypto_major avg `-0.364` n `8`; equity avg `-0.3407` n `66`; fx avg `-0.0031` n `6`; index avg `-0.504` n `23`; metal avg `-0.5831` n `18`; unknown avg `-0.557` n `383`
- 24h: commodity avg `0.6356` n `12`; crypto_alt avg `-1.1062` n `228`; crypto_major avg `-0.9742` n `8`; equity avg `-0.1335` n `66`; fx avg `-0.1159` n `6`; index avg `-0.7415` n `23`; metal avg `-2.1729` n `18`; unknown avg `0.819` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
