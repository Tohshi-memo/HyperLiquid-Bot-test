# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T02:07:29.161299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0152` n `12`; crypto_alt avg `-0.1933` n `229`; crypto_major avg `-0.21` n `8`; equity avg `0.2439` n `88`; fx avg `-0.018` n `6`; index avg `0.0876` n `25`; metal avg `0.0706` n `20`; unknown avg `0.2921` n `765`
- 1h: commodity avg `0.0895` n `12`; crypto_alt avg `0.4393` n `229`; crypto_major avg `0.4206` n `8`; equity avg `0.8104` n `88`; fx avg `-0.0318` n `6`; index avg `0.1846` n `25`; metal avg `0.178` n `20`; unknown avg `0.2442` n `765`
- 4h: commodity avg `0.1189` n `12`; crypto_alt avg `0.7389` n `229`; crypto_major avg `0.7878` n `8`; equity avg `1.1739` n `88`; fx avg `0.0312` n `6`; index avg `0.2718` n `25`; metal avg `0.6456` n `20`; unknown avg `0.3308` n `765`
- 24h: commodity avg `0.2829` n `12`; crypto_alt avg `2.3376` n `228`; crypto_major avg `3.4304` n `8`; equity avg `-1.3866` n `88`; fx avg `-0.1102` n `6`; index avg `-0.2809` n `25`; metal avg `1.4085` n `20`; unknown avg `5.6968` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
