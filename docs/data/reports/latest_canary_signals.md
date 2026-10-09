# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T11:37:30.118208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0313` n `13`; crypto_alt avg `0.4403` n `235`; crypto_major avg `0.3926` n `8`; equity avg `0.0963` n `150`; fx avg `0.0151` n `6`; index avg `0.0134` n `26`; metal avg `0.0229` n `20`; unknown avg `1.7538` n `1078`
- 1h: commodity avg `0.0234` n `13`; crypto_alt avg `0.404` n `235`; crypto_major avg `0.3031` n `8`; equity avg `0.1737` n `150`; fx avg `-0.0129` n `6`; index avg `0.0167` n `26`; metal avg `0.0804` n `20`; unknown avg `3.1834` n `1076`
- 4h: commodity avg `-0.0386` n `13`; crypto_alt avg `-0.4451` n `235`; crypto_major avg `-0.1467` n `8`; equity avg `0.0743` n `150`; fx avg `-0.0545` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0086` n `20`; unknown avg `0.3636` n `1006`
- 24h: commodity avg `-0.4918` n `13`; crypto_alt avg `-1.0604` n `235`; crypto_major avg `-1.0621` n `8`; equity avg `-0.0409` n `150`; fx avg `0.0611` n `6`; index avg `0.0899` n `26`; metal avg `0.5832` n `20`; unknown avg `7.6042` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
