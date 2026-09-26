# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T08:52:28.616360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `-0.0629` n `234`; crypto_major avg `-0.1741` n `8`; equity avg `-0.006` n `141`; fx avg `-0.0324` n `6`; index avg `0.0013` n `26`; metal avg `0.0037` n `20`; unknown avg `-0.0719` n `961`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.0662` n `234`; crypto_major avg `0.0212` n `8`; equity avg `0.0109` n `141`; fx avg `-0.0354` n `6`; index avg `0.0013` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.0957` n `943`
- 4h: commodity avg `-0.0691` n `12`; crypto_alt avg `0.6637` n `234`; crypto_major avg `-0.0712` n `8`; equity avg `0.0357` n `141`; fx avg `-0.0161` n `6`; index avg `-0.0017` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.0294` n `919`
- 24h: commodity avg `0.1262` n `12`; crypto_alt avg `2.5191` n `234`; crypto_major avg `0.4304` n `8`; equity avg `-0.8732` n `141`; fx avg `-0.1015` n `6`; index avg `-0.0026` n `26`; metal avg `0.0237` n `20`; unknown avg `1123.2527` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
