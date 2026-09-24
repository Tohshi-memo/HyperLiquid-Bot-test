# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T12:20:27.499638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0102` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1134` n `12`; crypto_alt avg `0.286` n `234`; crypto_major avg `0.2012` n `8`; equity avg `0.1811` n `141`; fx avg `0.002` n `6`; index avg `0.0296` n `26`; metal avg `0.0724` n `20`; unknown avg `0.9004` n `945`
- 1h: commodity avg `-0.1253` n `12`; crypto_alt avg `-0.0348` n `234`; crypto_major avg `0.0451` n `8`; equity avg `0.0369` n `141`; fx avg `-0.0269` n `6`; index avg `0.0123` n `26`; metal avg `0.0413` n `20`; unknown avg `0.1545` n `937`
- 4h: commodity avg `-0.2573` n `12`; crypto_alt avg `-1.0117` n `234`; crypto_major avg `-0.9799` n `8`; equity avg `0.0524` n `141`; fx avg `-0.0262` n `6`; index avg `0.0303` n `26`; metal avg `0.0482` n `20`; unknown avg `0.2941` n `937`
- 24h: commodity avg `0.3401` n `12`; crypto_alt avg `-4.028` n `234`; crypto_major avg `-3.2319` n `8`; equity avg `-1.7816` n `141`; fx avg `0.0022` n `6`; index avg `-0.3542` n `26`; metal avg `-0.3164` n `20`; unknown avg `587.5345` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
