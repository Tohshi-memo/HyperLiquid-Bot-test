# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T01:37:27.951964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.3599` n `234`; crypto_major avg `0.2938` n `8`; equity avg `0.0014` n `140`; fx avg `0.0004` n `6`; index avg `0.0119` n `26`; metal avg `0.0313` n `20`; unknown avg `0.0791` n `944`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.3031` n `234`; crypto_major avg `-0.6608` n `8`; equity avg `-0.2974` n `140`; fx avg `-0.0121` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0371` n `20`; unknown avg `-0.2622` n `942`
- 4h: commodity avg `0.1615` n `12`; crypto_alt avg `0.2641` n `234`; crypto_major avg `-0.9254` n `8`; equity avg `0.2473` n `140`; fx avg `-0.1422` n `6`; index avg `0.0707` n `26`; metal avg `0.0586` n `20`; unknown avg `0.8855` n `936`
- 24h: commodity avg `-0.1872` n `12`; crypto_alt avg `3.7619` n `234`; crypto_major avg `4.2575` n `8`; equity avg `2.1466` n `140`; fx avg `-0.2426` n `6`; index avg `0.5042` n `26`; metal avg `-0.0457` n `20`; unknown avg `13.1282` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
