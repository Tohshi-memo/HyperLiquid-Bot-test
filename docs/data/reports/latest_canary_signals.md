# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T01:07:25.058436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `0.1038` n `230`; crypto_major avg `0.0416` n `8`; equity avg `-0.0101` n `112`; fx avg `0.003` n `6`; index avg `-0.0051` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.0355` n `783`
- 1h: commodity avg `0.0378` n `12`; crypto_alt avg `0.0282` n `230`; crypto_major avg `0.0056` n `8`; equity avg `-0.0541` n `112`; fx avg `0.0056` n `6`; index avg `-0.0285` n `25`; metal avg `0.021` n `20`; unknown avg `-0.0945` n `783`
- 4h: commodity avg `-0.0498` n `12`; crypto_alt avg `-0.1775` n `230`; crypto_major avg `-0.1134` n `8`; equity avg `0.1204` n `112`; fx avg `0.0149` n `6`; index avg `-0.0333` n `25`; metal avg `0.0966` n `20`; unknown avg `-0.296` n `782`
- 24h: commodity avg `-0.1006` n `12`; crypto_alt avg `-0.6886` n `230`; crypto_major avg `-0.168` n `8`; equity avg `1.8717` n `112`; fx avg `-0.0951` n `6`; index avg `0.1041` n `25`; metal avg `0.5069` n `20`; unknown avg `-0.0975` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
