# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T10:07:37.894219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4862` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0346` n `12`; crypto_alt avg `-0.2454` n `234`; crypto_major avg `-0.1849` n `8`; equity avg `0.0966` n `141`; fx avg `0.0119` n `6`; index avg `0.01` n `26`; metal avg `-0.0178` n `20`; unknown avg `-0.1658` n `943`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.8691` n `234`; crypto_major avg `-0.8248` n `8`; equity avg `-0.0232` n `141`; fx avg `-0.0211` n `6`; index avg `-0.0221` n `26`; metal avg `-0.0917` n `20`; unknown avg `0.6952` n `943`
- 4h: commodity avg `0.2948` n `12`; crypto_alt avg `-1.8287` n `234`; crypto_major avg `-1.6124` n `8`; equity avg `-0.8095` n `141`; fx avg `0.0458` n `6`; index avg `-0.1262` n `26`; metal avg `-0.2074` n `20`; unknown avg `3.0735` n `937`
- 24h: commodity avg `0.8342` n `12`; crypto_alt avg `-5.4543` n `234`; crypto_major avg `-4.3454` n `8`; equity avg `-2.6823` n `141`; fx avg `0.0339` n `6`; index avg `-0.5071` n `26`; metal avg `-0.5644` n `20`; unknown avg `588.04` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
