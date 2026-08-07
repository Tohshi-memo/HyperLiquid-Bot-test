# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T10:30:20.116470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.0546` n `230`; crypto_major avg `0.034` n `8`; equity avg `0.1069` n `112`; fx avg `0.0011` n `6`; index avg `0.018` n `25`; metal avg `0.0137` n `20`; unknown avg `-0.0044` n `782`
- 1h: commodity avg `-0.099` n `12`; crypto_alt avg `-0.0025` n `230`; crypto_major avg `-0.0282` n `8`; equity avg `-0.1001` n `112`; fx avg `-0.0108` n `6`; index avg `-0.0167` n `25`; metal avg `-0.0533` n `20`; unknown avg `0.1024` n `782`
- 4h: commodity avg `-0.2842` n `12`; crypto_alt avg `0.0086` n `230`; crypto_major avg `0.6614` n `8`; equity avg `0.4555` n `112`; fx avg `-0.0266` n `6`; index avg `0.0628` n `25`; metal avg `0.106` n `20`; unknown avg `0.142` n `782`
- 24h: commodity avg `0.2036` n `12`; crypto_alt avg `0.655` n `230`; crypto_major avg `0.2724` n `8`; equity avg `1.9431` n `109`; fx avg `-0.0815` n `6`; index avg `0.0431` n `25`; metal avg `0.2626` n `20`; unknown avg `0.3259` n `765`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
