# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T20:09:22.134847+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.132` n `234`; crypto_major avg `0.3509` n `8`; equity avg `0.0285` n `140`; fx avg `-0.0075` n `6`; index avg `-0.0255` n `26`; metal avg `-0.0182` n `20`; unknown avg `254.0751` n `904`
- 1h: commodity avg `-0.0634` n `12`; crypto_alt avg `0.54` n `234`; crypto_major avg `0.4289` n `8`; equity avg `-0.122` n `140`; fx avg `-0.0086` n `6`; index avg `-0.0279` n `26`; metal avg `-0.0007` n `20`; unknown avg `14.7459` n `904`
- 4h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.1314` n `234`; crypto_major avg `0.7179` n `8`; equity avg `0.3023` n `140`; fx avg `-0.0079` n `6`; index avg `0.072` n `26`; metal avg `-0.0328` n `20`; unknown avg `7.5572` n `904`
- 24h: commodity avg `-1.0465` n `12`; crypto_alt avg `3.811` n `234`; crypto_major avg `5.4675` n `8`; equity avg `2.862` n `140`; fx avg `-0.0755` n `6`; index avg `0.6274` n `26`; metal avg `0.0399` n `20`; unknown avg `6.9259` n `719`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
