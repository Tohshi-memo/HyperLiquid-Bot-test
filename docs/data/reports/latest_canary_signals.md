# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T12:07:28.478767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1044` n `12`; crypto_alt avg `-0.2325` n `233`; crypto_major avg `-0.1675` n `8`; equity avg `-0.1033` n `136`; fx avg `0.0263` n `6`; index avg `-0.0207` n `26`; metal avg `-0.0271` n `20`; unknown avg `-0.03` n `794`
- 1h: commodity avg `0.108` n `12`; crypto_alt avg `0.4616` n `233`; crypto_major avg `0.2463` n `8`; equity avg `0.0149` n `136`; fx avg `0.0391` n `6`; index avg `0.0126` n `26`; metal avg `-0.0437` n `20`; unknown avg `0.1158` n `794`
- 4h: commodity avg `-0.2445` n `12`; crypto_alt avg `-1.0512` n `233`; crypto_major avg `-0.5592` n `8`; equity avg `0.1187` n `136`; fx avg `-0.0768` n `6`; index avg `0.0648` n `26`; metal avg `-0.0742` n `20`; unknown avg `-0.3091` n `788`
- 24h: commodity avg `0.0209` n `12`; crypto_alt avg `-1.8567` n `233`; crypto_major avg `-1.6937` n `8`; equity avg `-0.544` n `136`; fx avg `-0.0711` n `6`; index avg `0.0012` n `26`; metal avg `-0.4027` n `20`; unknown avg `1.4872` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
