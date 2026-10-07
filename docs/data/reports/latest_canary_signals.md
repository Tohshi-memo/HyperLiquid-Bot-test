# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T17:22:27.341369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0931` n `13`; crypto_alt avg `-0.0123` n `235`; crypto_major avg `-0.111` n `8`; equity avg `0.0947` n `150`; fx avg `0.0088` n `6`; index avg `0.0187` n `26`; metal avg `0.0232` n `20`; unknown avg `1.3862` n `1077`
- 1h: commodity avg `-0.1793` n `13`; crypto_alt avg `-0.2475` n `235`; crypto_major avg `-0.3417` n `8`; equity avg `0.1209` n `150`; fx avg `-0.0158` n `6`; index avg `0.0346` n `26`; metal avg `0.0451` n `20`; unknown avg `1.1073` n `1074`
- 4h: commodity avg `-0.3653` n `13`; crypto_alt avg `0.3541` n `235`; crypto_major avg `-0.0551` n `8`; equity avg `0.3722` n `150`; fx avg `-0.0092` n `6`; index avg `0.0989` n `26`; metal avg `0.1708` n `20`; unknown avg `0.118` n `1022`
- 24h: commodity avg `0.4476` n `13`; crypto_alt avg `-4.6174` n `235`; crypto_major avg `-3.2733` n `8`; equity avg `-1.3636` n `150`; fx avg `-0.176` n `6`; index avg `-0.2186` n `26`; metal avg `-0.4957` n `20`; unknown avg `15.1234` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1438`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1363`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1356`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0855`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0707`, n `669`, weak_sample_signal
