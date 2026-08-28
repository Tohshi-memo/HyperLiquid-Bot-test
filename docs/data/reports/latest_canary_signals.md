# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T00:52:26.720993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.0774` n `231`; crypto_major avg `-0.2144` n `8`; equity avg `0.1017` n `127`; fx avg `0.0098` n `6`; index avg `0.0221` n `26`; metal avg `-0.0073` n `20`; unknown avg `-0.0692` n `792`
- 1h: commodity avg `-0.0011` n `12`; crypto_alt avg `0.32` n `231`; crypto_major avg `-0.2102` n `8`; equity avg `0.3091` n `127`; fx avg `-0.0257` n `6`; index avg `0.1017` n `26`; metal avg `-0.0615` n `20`; unknown avg `0.0532` n `792`
- 4h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.515` n `231`; crypto_major avg `0.0676` n `8`; equity avg `-0.0772` n `127`; fx avg `-0.0279` n `6`; index avg `0.0596` n `26`; metal avg `-0.0958` n `20`; unknown avg `-0.0544` n `792`
- 24h: commodity avg `0.3451` n `12`; crypto_alt avg `1.7617` n `231`; crypto_major avg `2.6276` n `8`; equity avg `0.6388` n `127`; fx avg `0.0312` n `6`; index avg `0.1308` n `26`; metal avg `0.0487` n `20`; unknown avg `0.8647` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
