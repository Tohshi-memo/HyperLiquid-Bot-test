# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T05:37:12.811872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1309` n `12`; crypto_alt avg `-0.1564` n `228`; crypto_major avg `0.0575` n `8`; equity avg `0.1555` n `66`; fx avg `-0.0108` n `5`; index avg `0.1513` n `23`; metal avg `0.0392` n `18`; unknown avg `4.4181` n `383`
- 1h: commodity avg `-0.1017` n `12`; crypto_alt avg `0.0016` n `228`; crypto_major avg `0.1939` n `8`; equity avg `0.2034` n `66`; fx avg `-0.0206` n `5`; index avg `0.0962` n `23`; metal avg `0.0779` n `18`; unknown avg `1.0724` n `383`
- 4h: commodity avg `-0.2882` n `12`; crypto_alt avg `0.496` n `228`; crypto_major avg `0.2092` n `8`; equity avg `0.7042` n `66`; fx avg `0.0053` n `5`; index avg `0.3405` n `23`; metal avg `0.7995` n `18`; unknown avg `1.0814` n `383`
- 24h: commodity avg `2.597` n `12`; crypto_alt avg `-10.9388` n `228`; crypto_major avg `-3.2647` n `8`; equity avg `-2.9904` n `65`; fx avg `-0.0876` n `5`; index avg `-1.6855` n `23`; metal avg `-6.0212` n `18`; unknown avg `549.9947` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
