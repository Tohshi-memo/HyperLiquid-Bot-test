# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T10:37:26.523641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `3.5725` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0352` n `12`; crypto_alt avg `-0.3294` n `232`; crypto_major avg `-0.3962` n `8`; equity avg `-0.0872` n `133`; fx avg `0.0064` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0121` n `20`; unknown avg `-0.0838` n `792`
- 1h: commodity avg `0.2364` n `12`; crypto_alt avg `-0.3075` n `232`; crypto_major avg `-0.3005` n `8`; equity avg `-0.233` n `133`; fx avg `-0.0023` n `6`; index avg `3.272` n `26`; metal avg `-0.1072` n `20`; unknown avg `-0.1675` n `790`
- 4h: commodity avg `0.4666` n `12`; crypto_alt avg `-0.116` n `232`; crypto_major avg `-0.4094` n `8`; equity avg `-0.299` n `133`; fx avg `-0.0843` n `6`; index avg `-0.0796` n `26`; metal avg `-0.0385` n `20`; unknown avg `-0.0758` n `790`
- 24h: commodity avg `0.5567` n `12`; crypto_alt avg `1.8543` n `232`; crypto_major avg `1.56` n `8`; equity avg `1.494` n `133`; fx avg `-0.3868` n `6`; index avg `0.128` n `26`; metal avg `0.7857` n `20`; unknown avg `-0.2442` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0455`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0415`, n `668`, weak_sample_signal
