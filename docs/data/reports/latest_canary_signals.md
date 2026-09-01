# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T07:52:24.937587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `-0.0755` n `232`; crypto_major avg `0.0189` n `8`; equity avg `-0.1889` n `130`; fx avg `0.0083` n `6`; index avg `-0.0165` n `26`; metal avg `-0.0097` n `20`; unknown avg `0.0366` n `792`
- 1h: commodity avg `0.1398` n `12`; crypto_alt avg `-0.1112` n `232`; crypto_major avg `-0.3421` n `8`; equity avg `-0.2148` n `130`; fx avg `0.0046` n `6`; index avg `-0.036` n `26`; metal avg `-0.0763` n `20`; unknown avg `0.1263` n `790`
- 4h: commodity avg `0.1099` n `12`; crypto_alt avg `0.0681` n `232`; crypto_major avg `-0.3665` n `8`; equity avg `-0.0773` n `130`; fx avg `-0.0032` n `6`; index avg `-0.0023` n `26`; metal avg `-0.1647` n `20`; unknown avg `0.1445` n `770`
- 24h: commodity avg `0.5761` n `12`; crypto_alt avg `1.2417` n `232`; crypto_major avg `0.8007` n `8`; equity avg `0.2752` n `130`; fx avg `0.0544` n `6`; index avg `-0.0521` n `26`; metal avg `-0.2761` n `20`; unknown avg `0.2849` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
