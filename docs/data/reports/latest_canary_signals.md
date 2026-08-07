# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T22:07:31.315860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0226` n `12`; crypto_alt avg `-0.0702` n `230`; crypto_major avg `-0.0189` n `8`; equity avg `0.018` n `112`; fx avg `0.0181` n `6`; index avg `0.0019` n `25`; metal avg `0.0277` n `20`; unknown avg `0.0585` n `782`
- 1h: commodity avg `-0.0851` n `12`; crypto_alt avg `-0.2515` n `230`; crypto_major avg `-0.1044` n `8`; equity avg `0.012` n `112`; fx avg `0.0197` n `6`; index avg `-0.0157` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.0734` n `782`
- 4h: commodity avg `-0.3628` n `12`; crypto_alt avg `-0.2806` n `230`; crypto_major avg `0.1035` n `8`; equity avg `0.3941` n `112`; fx avg `0.0324` n `6`; index avg `0.0486` n `25`; metal avg `0.0582` n `20`; unknown avg `-0.1551` n `782`
- 24h: commodity avg `-0.1788` n `12`; crypto_alt avg `-0.6611` n `230`; crypto_major avg `-0.1526` n `8`; equity avg `1.6875` n `112`; fx avg `-0.1147` n `6`; index avg `0.0844` n `25`; metal avg `0.4819` n `20`; unknown avg `0.0825` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
