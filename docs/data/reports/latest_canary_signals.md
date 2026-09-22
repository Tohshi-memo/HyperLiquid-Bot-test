# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T03:52:29.858111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.053` n `12`; crypto_alt avg `-0.0412` n `234`; crypto_major avg `0.0328` n `8`; equity avg `-0.1807` n `140`; fx avg `0.0138` n `6`; index avg `-0.018` n `26`; metal avg `-0.0364` n `20`; unknown avg `1.4454` n `944`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0915` n `234`; crypto_major avg `-0.0007` n `8`; equity avg `-0.1054` n `140`; fx avg `-0.017` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0478` n `20`; unknown avg `2.0775` n `942`
- 4h: commodity avg `0.1378` n `12`; crypto_alt avg `-0.0165` n `234`; crypto_major avg `-0.8097` n `8`; equity avg `-0.0224` n `140`; fx avg `-0.1567` n `6`; index avg `-0.0069` n `26`; metal avg `-0.2088` n `20`; unknown avg `0.7994` n `936`
- 24h: commodity avg `-0.1815` n `12`; crypto_alt avg `2.8081` n `234`; crypto_major avg `4.141` n `8`; equity avg `2.2968` n `140`; fx avg `-0.2211` n `6`; index avg `0.4629` n `26`; metal avg `-0.0698` n `20`; unknown avg `8.455` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
