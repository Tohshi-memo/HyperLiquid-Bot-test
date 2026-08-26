# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T20:22:28.462578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.5057` n `231`; crypto_major avg `-0.6201` n `8`; equity avg `-0.3272` n `122`; fx avg `-0.0027` n `6`; index avg `-0.0356` n `25`; metal avg `-0.0555` n `20`; unknown avg `-0.1633` n `797`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.4397` n `231`; crypto_major avg `-0.4488` n `8`; equity avg `-0.1103` n `122`; fx avg `0.0015` n `6`; index avg `-0.0326` n `25`; metal avg `-0.0446` n `20`; unknown avg `-0.1358` n `797`
- 4h: commodity avg `-0.299` n `12`; crypto_alt avg `0.1133` n `231`; crypto_major avg `0.0946` n `8`; equity avg `0.3509` n `122`; fx avg `-0.0166` n `6`; index avg `0.0315` n `25`; metal avg `-0.0673` n `20`; unknown avg `-0.0214` n `797`
- 24h: commodity avg `0.4889` n `12`; crypto_alt avg `-1.5953` n `231`; crypto_major avg `-1.7492` n `8`; equity avg `-0.3223` n `122`; fx avg `-0.0559` n `6`; index avg `-0.0188` n `25`; metal avg `-0.4909` n `20`; unknown avg `0.4301` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
