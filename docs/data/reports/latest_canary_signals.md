# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T09:22:23.662032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `0.0312` n `230`; crypto_major avg `0.0443` n `8`; equity avg `0.0188` n `112`; fx avg `0.0031` n `6`; index avg `0.0031` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.0078` n `784`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `0.1126` n `230`; crypto_major avg `0.2235` n `8`; equity avg `0.0448` n `112`; fx avg `0.0084` n `6`; index avg `0.0192` n `25`; metal avg `0.0164` n `20`; unknown avg `0.1031` n `784`
- 4h: commodity avg `0.0417` n `12`; crypto_alt avg `0.2431` n `230`; crypto_major avg `0.2494` n `8`; equity avg `0.0583` n `112`; fx avg `0.0012` n `6`; index avg `0.0105` n `25`; metal avg `0.0325` n `20`; unknown avg `0.1342` n `752`
- 24h: commodity avg `-0.0683` n `12`; crypto_alt avg `0.1027` n `230`; crypto_major avg `0.2789` n `8`; equity avg `0.6883` n `112`; fx avg `-0.0336` n `6`; index avg `0.0449` n `25`; metal avg `-0.1078` n `20`; unknown avg `0.1063` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
