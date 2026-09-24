# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T12:07:31.446337+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5471` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `0.1298` n `234`; crypto_major avg `0.135` n `8`; equity avg `0.0364` n `141`; fx avg `-0.0183` n `6`; index avg `0.0194` n `26`; metal avg `-0.0034` n `20`; unknown avg `7.7472` n `937`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.1286` n `234`; crypto_major avg `-0.1182` n `8`; equity avg `-0.1273` n `141`; fx avg `-0.0259` n `6`; index avg `-0.0077` n `26`; metal avg `0.0598` n `20`; unknown avg `2.3602` n `937`
- 4h: commodity avg `0.0039` n `12`; crypto_alt avg `-1.729` n `234`; crypto_major avg `-1.5979` n `8`; equity avg `-0.4554` n `141`; fx avg `0.0142` n `6`; index avg `-0.0508` n `26`; metal avg `-0.207` n `20`; unknown avg `0.5232` n `937`
- 24h: commodity avg `0.4911` n `12`; crypto_alt avg `-4.2208` n `234`; crypto_major avg `-3.4367` n `8`; equity avg `-1.9712` n `141`; fx avg `-0.0021` n `6`; index avg `-0.3926` n `26`; metal avg `-0.4226` n `20`; unknown avg `587.4152` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
