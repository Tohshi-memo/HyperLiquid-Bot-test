# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T02:37:25.093250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.0174` n `230`; crypto_major avg `-0.0871` n `8`; equity avg `0.0569` n `121`; fx avg `-0.0092` n `6`; index avg `0.0252` n `25`; metal avg `0.0145` n `20`; unknown avg `0.0425` n `792`
- 1h: commodity avg `-0.0589` n `12`; crypto_alt avg `-0.0801` n `230`; crypto_major avg `0.0622` n `8`; equity avg `-0.0166` n `121`; fx avg `-0.0159` n `6`; index avg `0.028` n `25`; metal avg `0.0149` n `20`; unknown avg `0.0364` n `792`
- 4h: commodity avg `0.06` n `12`; crypto_alt avg `0.289` n `230`; crypto_major avg `-0.4445` n `8`; equity avg `0.1498` n `121`; fx avg `0.0996` n `6`; index avg `0.1044` n `25`; metal avg `-0.1486` n `20`; unknown avg `0.0545` n `792`
- 24h: commodity avg `-0.1017` n `12`; crypto_alt avg `5.5811` n `230`; crypto_major avg `9.8605` n `8`; equity avg `0.9837` n `120`; fx avg `0.0006` n `6`; index avg `0.3047` n `25`; metal avg `1.0172` n `20`; unknown avg `1.6286` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
