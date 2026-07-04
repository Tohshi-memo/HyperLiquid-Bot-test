# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T23:07:25.071901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.025` n `229`; crypto_major avg `0.0109` n `8`; equity avg `0.0099` n `88`; fx avg `0.0007` n `6`; index avg `-0.0022` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.1274` n `765`
- 1h: commodity avg `0.0305` n `12`; crypto_alt avg `-0.3197` n `229`; crypto_major avg `-0.0985` n `8`; equity avg `0.0335` n `88`; fx avg `0.0102` n `6`; index avg `0.0112` n `25`; metal avg `-0.0095` n `20`; unknown avg `-0.2506` n `765`
- 4h: commodity avg `0.0197` n `12`; crypto_alt avg `-0.605` n `229`; crypto_major avg `-0.3729` n `8`; equity avg `0.1395` n `88`; fx avg `-0.0167` n `6`; index avg `0.0359` n `25`; metal avg `0.0365` n `20`; unknown avg `0.3112` n `765`
- 24h: commodity avg `0.0358` n `12`; crypto_alt avg `0.0566` n `229`; crypto_major avg `0.6541` n `8`; equity avg `0.3419` n `88`; fx avg `-0.0149` n `6`; index avg `0.0004` n `25`; metal avg `0.0731` n `20`; unknown avg `-0.4188` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
