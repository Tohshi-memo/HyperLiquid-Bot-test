# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T14:22:42.487813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.0988` n `229`; crypto_major avg `0.0451` n `8`; equity avg `-0.0076` n `88`; fx avg `0.0096` n `6`; index avg `0.0124` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0` n `765`
- 1h: commodity avg `-0.042` n `12`; crypto_alt avg `-0.1636` n `229`; crypto_major avg `0.0095` n `8`; equity avg `-0.0302` n `88`; fx avg `0.0037` n `6`; index avg `0.0128` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.1012` n `765`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `0.7205` n `229`; crypto_major avg `0.4505` n `8`; equity avg `-0.092` n `88`; fx avg `0.0096` n `6`; index avg `0.0077` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0985` n `759`
- 24h: commodity avg `-0.025` n `12`; crypto_alt avg `1.0856` n `229`; crypto_major avg `1.9105` n `8`; equity avg `0.2966` n `88`; fx avg `-0.0444` n `6`; index avg `-0.0467` n `25`; metal avg `0.0099` n `20`; unknown avg `2.5602` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
