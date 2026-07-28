# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T07:52:32.202200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1139` n `12`; crypto_alt avg `-0.1628` n `230`; crypto_major avg `0.0239` n `8`; equity avg `0.0251` n `102`; fx avg `-0.0115` n `6`; index avg `-0.0432` n `25`; metal avg `0.0094` n `20`; unknown avg `0.0182` n `774`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.3785` n `230`; crypto_major avg `-0.2222` n `8`; equity avg `-0.0411` n `102`; fx avg `0.0123` n `6`; index avg `-0.009` n `25`; metal avg `0.0035` n `20`; unknown avg `0.0328` n `774`
- 4h: commodity avg `-0.1912` n `12`; crypto_alt avg `-0.156` n `230`; crypto_major avg `-0.1756` n `8`; equity avg `-0.4623` n `102`; fx avg `-0.0622` n `6`; index avg `-0.1078` n `25`; metal avg `-0.0203` n `20`; unknown avg `-0.0356` n `758`
- 24h: commodity avg `-0.6977` n `12`; crypto_alt avg `-3.8743` n `230`; crypto_major avg `-3.6446` n `8`; equity avg `-4.0961` n `102`; fx avg `-0.1779` n `6`; index avg `-0.8642` n `25`; metal avg `-0.4007` n `20`; unknown avg `1158.5901` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
