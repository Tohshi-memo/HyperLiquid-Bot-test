# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T22:37:26.678343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.0597` n `235`; crypto_major avg `-0.0879` n `8`; equity avg `0.0011` n `150`; fx avg `-0.0007` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.0118` n `1076`
- 1h: commodity avg `0.0393` n `13`; crypto_alt avg `-0.2047` n `235`; crypto_major avg `-0.0766` n `8`; equity avg `0.0385` n `150`; fx avg `-0.0065` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0243` n `20`; unknown avg `0.0114` n `1058`
- 4h: commodity avg `0.2455` n `13`; crypto_alt avg `-0.3884` n `235`; crypto_major avg `-0.181` n `8`; equity avg `-0.0452` n `150`; fx avg `-0.0009` n `6`; index avg `-0.019` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.1934` n `990`
- 24h: commodity avg `0.324` n `13`; crypto_alt avg `-1.5239` n `235`; crypto_major avg `-1.1045` n `8`; equity avg `0.3919` n `149`; fx avg `0.0825` n `6`; index avg `-0.0063` n `26`; metal avg `-0.006` n `20`; unknown avg `871.0887` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
