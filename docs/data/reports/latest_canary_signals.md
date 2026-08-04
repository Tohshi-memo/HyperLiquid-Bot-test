# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T23:07:34.170551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.0859` n `230`; crypto_major avg `0.1395` n `8`; equity avg `0.0938` n `108`; fx avg `0.0059` n `6`; index avg `0.0261` n `25`; metal avg `-0.0521` n `20`; unknown avg `0.212` n `781`
- 1h: commodity avg `0.0237` n `12`; crypto_alt avg `0.1512` n `230`; crypto_major avg `0.102` n `8`; equity avg `0.1102` n `108`; fx avg `0.0046` n `6`; index avg `0.0296` n `25`; metal avg `-0.0301` n `20`; unknown avg `0.3581` n `781`
- 4h: commodity avg `-0.0753` n `12`; crypto_alt avg `0.081` n `230`; crypto_major avg `-0.0115` n `8`; equity avg `-0.5392` n `108`; fx avg `0.0056` n `6`; index avg `-0.0465` n `25`; metal avg `-0.0825` n `20`; unknown avg `0.4735` n `781`
- 24h: commodity avg `-1.2639` n `12`; crypto_alt avg `0.2731` n `230`; crypto_major avg `0.8777` n `8`; equity avg `3.051` n `107`; fx avg `0.1151` n `6`; index avg `0.727` n `25`; metal avg `0.858` n `20`; unknown avg `0.4489` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
