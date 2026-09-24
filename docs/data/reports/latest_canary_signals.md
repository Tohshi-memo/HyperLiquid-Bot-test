# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T23:34:57.843583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.0124` n `234`; crypto_major avg `0.065` n `8`; equity avg `0.0035` n `141`; fx avg `0.0013` n `6`; index avg `0.0194` n `26`; metal avg `-0.0042` n `20`; unknown avg `2.9058` n `946`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `0.1741` n `234`; crypto_major avg `0.2456` n `8`; equity avg `0.0124` n `141`; fx avg `0.0426` n `6`; index avg `0.0025` n `26`; metal avg `0.0078` n `20`; unknown avg `7.4329` n `944`
- 4h: commodity avg `-0.4775` n `12`; crypto_alt avg `-0.1491` n `234`; crypto_major avg `-0.3274` n `8`; equity avg `0.0157` n `141`; fx avg `0.0062` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0206` n `20`; unknown avg `12.0501` n `836`
- 24h: commodity avg `0.6187` n `12`; crypto_alt avg `3.9974` n `234`; crypto_major avg `1.0305` n `8`; equity avg `-0.3038` n `141`; fx avg `0.0624` n `6`; index avg `-0.1033` n `26`; metal avg `-0.0778` n `20`; unknown avg `24.6502` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
