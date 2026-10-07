# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T21:22:32.458374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0352` n `13`; crypto_alt avg `-0.0272` n `235`; crypto_major avg `-0.0406` n `8`; equity avg `0.0336` n `150`; fx avg `-0.0048` n `6`; index avg `0.0081` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.051` n `1077`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `0.0546` n `235`; crypto_major avg `-0.1483` n `8`; equity avg `0.0453` n `150`; fx avg `0.0064` n `6`; index avg `0.0134` n `26`; metal avg `0.0167` n `20`; unknown avg `-0.2042` n `1025`
- 4h: commodity avg `0.227` n `13`; crypto_alt avg `0.4451` n `235`; crypto_major avg `-0.1187` n `8`; equity avg `-0.0248` n `150`; fx avg `0.0325` n `6`; index avg `-0.0126` n `26`; metal avg `-0.1279` n `20`; unknown avg `0.4365` n `999`
- 24h: commodity avg `0.3955` n `13`; crypto_alt avg `-3.9527` n `235`; crypto_major avg `-3.3389` n `8`; equity avg `-1.3787` n `150`; fx avg `-0.1466` n `6`; index avg `-0.214` n `26`; metal avg `-0.6847` n `20`; unknown avg `1.1213` n `972`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
