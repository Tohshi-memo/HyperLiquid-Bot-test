# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T13:07:30.827564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `0.1586` n `232`; crypto_major avg `0.2179` n `8`; equity avg `-0.0747` n `128`; fx avg `0.0046` n `6`; index avg `-0.0089` n `26`; metal avg `-0.001` n `20`; unknown avg `1.0818` n `792`
- 1h: commodity avg `-0.1814` n `12`; crypto_alt avg `-0.6223` n `232`; crypto_major avg `-0.4092` n `8`; equity avg `-0.4322` n `128`; fx avg `0.0306` n `6`; index avg `-0.0574` n `26`; metal avg `-0.2252` n `20`; unknown avg `1.9759` n `792`
- 4h: commodity avg `-0.0881` n `12`; crypto_alt avg `-0.3908` n `232`; crypto_major avg `-0.1735` n `8`; equity avg `-0.5112` n `128`; fx avg `0.0247` n `6`; index avg `-0.0888` n `26`; metal avg `-0.1206` n `20`; unknown avg `1.3128` n `791`
- 24h: commodity avg `0.4355` n `12`; crypto_alt avg `-1.5407` n `231`; crypto_major avg `-1.783` n `8`; equity avg `-0.8384` n `128`; fx avg `-0.1062` n `6`; index avg `-0.1471` n `26`; metal avg `-0.3426` n `20`; unknown avg `0.9659` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
