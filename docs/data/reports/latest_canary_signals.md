# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T07:22:32.295721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.1175` n `232`; crypto_major avg `-0.0636` n `8`; equity avg `0.0436` n `132`; fx avg `-0.0025` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.1045` n `792`
- 1h: commodity avg `-0.1023` n `12`; crypto_alt avg `0.2359` n `232`; crypto_major avg `0.1139` n `8`; equity avg `0.1693` n `132`; fx avg `-0.0134` n `6`; index avg `0.0542` n `26`; metal avg `0.0292` n `20`; unknown avg `0.1356` n `788`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.0856` n `232`; crypto_major avg `-0.0075` n `8`; equity avg `0.0825` n `132`; fx avg `-0.1109` n `6`; index avg `-0.0064` n `26`; metal avg `0.1968` n `20`; unknown avg `0.1738` n `770`
- 24h: commodity avg `0.614` n `12`; crypto_alt avg `-0.8534` n `232`; crypto_major avg `-1.6769` n `8`; equity avg `-2.4743` n `130`; fx avg `-0.1889` n `6`; index avg `-0.4618` n `26`; metal avg `-0.9168` n `20`; unknown avg `-0.1581` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0542`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
