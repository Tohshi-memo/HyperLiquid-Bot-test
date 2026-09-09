# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T19:07:33.039286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1792` n `233`; crypto_major avg `-0.1768` n `8`; equity avg `-0.0441` n `134`; fx avg `-0.0069` n `6`; index avg `-0.009` n `26`; metal avg `-0.045` n `20`; unknown avg `14.4888` n `795`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.3197` n `233`; crypto_major avg `-0.378` n `8`; equity avg `-0.189` n `134`; fx avg `-0.0026` n `6`; index avg `-0.0095` n `26`; metal avg `-0.1423` n `20`; unknown avg `9.736` n `795`
- 4h: commodity avg `-0.1404` n `12`; crypto_alt avg `-0.1699` n `233`; crypto_major avg `-0.1723` n `8`; equity avg `-0.2822` n `134`; fx avg `0.0082` n `6`; index avg `-0.0342` n `26`; metal avg `0.0207` n `20`; unknown avg `1.2196` n `789`
- 24h: commodity avg `0.0938` n `12`; crypto_alt avg `-0.5147` n `233`; crypto_major avg `-0.3748` n `8`; equity avg `-0.5911` n `134`; fx avg `-0.0245` n `6`; index avg `-0.1989` n `26`; metal avg `0.412` n `20`; unknown avg `4.3551` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
