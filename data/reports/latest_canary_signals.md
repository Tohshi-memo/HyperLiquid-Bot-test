# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T00:52:27.802259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.2582` n `234`; crypto_major avg `0.02` n `8`; equity avg `-0.001` n `140`; fx avg `-0.0362` n `6`; index avg `-0.013` n `26`; metal avg `0.0217` n `20`; unknown avg `-0.2093` n `944`
- 1h: commodity avg `0.0976` n `12`; crypto_alt avg `0.777` n `234`; crypto_major avg `0.209` n `8`; equity avg `0.2445` n `140`; fx avg `-0.1582` n `6`; index avg `0.0348` n `26`; metal avg `-0.0323` n `20`; unknown avg `0.5479` n `936`
- 4h: commodity avg `0.1461` n `12`; crypto_alt avg `0.9344` n `234`; crypto_major avg `-0.1421` n `8`; equity avg `0.642` n `140`; fx avg `-0.1671` n `6`; index avg `0.0765` n `26`; metal avg `0.1166` n `20`; unknown avg `0.2987` n `936`
- 24h: commodity avg `-0.3276` n `12`; crypto_alt avg `3.9536` n `234`; crypto_major avg `4.5717` n `8`; equity avg `2.6` n `140`; fx avg `-0.2577` n `6`; index avg `0.5484` n `26`; metal avg `0.115` n `20`; unknown avg `13.2893` n `771`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
