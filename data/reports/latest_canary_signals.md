# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T22:37:32.864596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0356` n `12`; crypto_alt avg `-0.4582` n `234`; crypto_major avg `-0.215` n `8`; equity avg `-0.0732` n `141`; fx avg `-0.0065` n `6`; index avg `-0.0234` n `26`; metal avg `0.0076` n `20`; unknown avg `0.0194` n `945`
- 1h: commodity avg `-0.0623` n `12`; crypto_alt avg `-0.3096` n `234`; crypto_major avg `0.1071` n `8`; equity avg `0.0676` n `141`; fx avg `-0.0033` n `6`; index avg `0.0113` n `26`; metal avg `0.0229` n `20`; unknown avg `1.2821` n `943`
- 4h: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.1821` n `234`; crypto_major avg `0.4605` n `8`; equity avg `-0.1431` n `141`; fx avg `-0.0126` n `6`; index avg `0.0088` n `26`; metal avg `0.0412` n `20`; unknown avg `-0.2113` n `845`
- 24h: commodity avg `0.5529` n `12`; crypto_alt avg `-4.2291` n `234`; crypto_major avg `-3.2993` n `8`; equity avg `-1.6424` n `140`; fx avg `-0.0121` n `6`; index avg `-0.3619` n `26`; metal avg `-0.8096` n `20`; unknown avg `584.2959` n `821`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
