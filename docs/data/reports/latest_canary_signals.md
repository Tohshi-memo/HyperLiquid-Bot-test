# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T13:37:27.635815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2693` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0504` n `12`; crypto_alt avg `0.4763` n `228`; crypto_major avg `0.387` n `8`; equity avg `0.4829` n `86`; fx avg `-0.0094` n `6`; index avg `0.0354` n `23`; metal avg `-0.0927` n `20`; unknown avg `0.0258` n `765`
- 1h: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.4039` n `228`; crypto_major avg `-0.4401` n `8`; equity avg `-0.0044` n `86`; fx avg `0.0238` n `6`; index avg `-0.0417` n `23`; metal avg `-0.072` n `20`; unknown avg `-0.0099` n `765`
- 4h: commodity avg `0.062` n `12`; crypto_alt avg `-1.1196` n `228`; crypto_major avg `-1.326` n `8`; equity avg `-0.1774` n `86`; fx avg `0.014` n `6`; index avg `-0.0567` n `23`; metal avg `-0.0856` n `20`; unknown avg `-0.0528` n `765`
- 24h: commodity avg `-0.0529` n `12`; crypto_alt avg `-1.8124` n `228`; crypto_major avg `-1.9546` n `8`; equity avg `-3.5357` n `86`; fx avg `0.0591` n `6`; index avg `-0.6612` n `23`; metal avg `0.1908` n `20`; unknown avg `0.7656` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3406`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2098`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
