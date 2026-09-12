# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T05:52:29.680740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.78` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0136` n `12`; crypto_alt avg `-0.1047` n `233`; crypto_major avg `-0.004` n `8`; equity avg `-0.0163` n `136`; fx avg `-0.0008` n `6`; index avg `0.0069` n `26`; metal avg `-0.0054` n `20`; unknown avg `31.3129` n `838`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.032` n `233`; crypto_major avg `-0.0156` n `8`; equity avg `-0.0196` n `136`; fx avg `-0.0049` n `6`; index avg `0.0072` n `26`; metal avg `0.0037` n `20`; unknown avg `14.8405` n `836`
- 4h: commodity avg `-0.0611` n `12`; crypto_alt avg `0.0466` n `233`; crypto_major avg `-0.0249` n `8`; equity avg `-0.1073` n `136`; fx avg `-0.0031` n `6`; index avg `0.009` n `26`; metal avg `-0.0064` n `20`; unknown avg `2.4996` n `818`
- 24h: commodity avg `-0.3941` n `12`; crypto_alt avg `0.8141` n `233`; crypto_major avg `0.7678` n `8`; equity avg `0.5071` n `136`; fx avg `-0.1083` n `6`; index avg `0.2078` n `26`; metal avg `-0.0023` n `20`; unknown avg `1.338` n `690`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
