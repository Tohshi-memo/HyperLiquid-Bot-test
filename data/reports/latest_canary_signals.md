# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T10:52:28.411061+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0427` n `12`; crypto_alt avg `0.3173` n `232`; crypto_major avg `0.3604` n `8`; equity avg `0.0703` n `128`; fx avg `-0.005` n `6`; index avg `0.0123` n `26`; metal avg `0.0547` n `20`; unknown avg `-0.0112` n `794`
- 1h: commodity avg `-0.0293` n `12`; crypto_alt avg `0.3463` n `232`; crypto_major avg `0.4154` n `8`; equity avg `0.1056` n `128`; fx avg `-0.0189` n `6`; index avg `0.0081` n `26`; metal avg `0.0891` n `20`; unknown avg `0.0585` n `792`
- 4h: commodity avg `0.2187` n `12`; crypto_alt avg `0.338` n `232`; crypto_major avg `0.7382` n `8`; equity avg `-0.2783` n `128`; fx avg `-0.0309` n `6`; index avg `-0.0412` n `26`; metal avg `0.0285` n `20`; unknown avg `0.3245` n `791`
- 24h: commodity avg `0.6146` n `12`; crypto_alt avg `-0.1867` n `231`; crypto_major avg `-0.7026` n `8`; equity avg `-0.3756` n `128`; fx avg `-0.1291` n `6`; index avg `-0.0648` n `26`; metal avg `-0.1713` n `20`; unknown avg `-0.0867` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0494`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0457`, n `668`, weak_sample_signal
