# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T12:22:23.537115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0378` n `12`; crypto_alt avg `-0.1894` n `232`; crypto_major avg `-0.0941` n `8`; equity avg `-0.0977` n `130`; fx avg `-0.0` n `6`; index avg `-0.0054` n `26`; metal avg `0.0299` n `20`; unknown avg `0.0221` n `792`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.072` n `232`; crypto_major avg `0.0647` n `8`; equity avg `-0.2543` n `130`; fx avg `-0.0009` n `6`; index avg `-0.0379` n `26`; metal avg `0.0405` n `20`; unknown avg `-0.0325` n `790`
- 4h: commodity avg `-0.123` n `12`; crypto_alt avg `0.1093` n `232`; crypto_major avg `0.0072` n `8`; equity avg `-0.9148` n `130`; fx avg `0.0266` n `6`; index avg `-0.1858` n `26`; metal avg `-0.2634` n `20`; unknown avg `-0.2868` n `790`
- 24h: commodity avg `0.3084` n `12`; crypto_alt avg `0.6935` n `232`; crypto_major avg `0.0414` n `8`; equity avg `-1.0251` n `130`; fx avg `0.0927` n `6`; index avg `-0.3131` n `26`; metal avg `-0.7457` n `20`; unknown avg `-0.1889` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0331`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0295`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0282`, n `668`, weak_sample_signal
