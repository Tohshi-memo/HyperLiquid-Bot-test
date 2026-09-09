# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T18:07:26.370760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0682` n `12`; crypto_alt avg `-0.0396` n `233`; crypto_major avg `-0.0514` n `8`; equity avg `0.0006` n `134`; fx avg `-0.0157` n `6`; index avg `-0.0055` n `26`; metal avg `0.0063` n `20`; unknown avg `9.6861` n `795`
- 1h: commodity avg `0.117` n `12`; crypto_alt avg `-0.0275` n `233`; crypto_major avg `0.1408` n `8`; equity avg `0.0402` n `134`; fx avg `-0.0009` n `6`; index avg `0.0042` n `26`; metal avg `-0.0749` n `20`; unknown avg `10.7954` n `795`
- 4h: commodity avg `0.0181` n `12`; crypto_alt avg `-0.521` n `233`; crypto_major avg `-0.3808` n `8`; equity avg `-0.4705` n `134`; fx avg `0.0425` n `6`; index avg `-0.1588` n `26`; metal avg `-0.0068` n `20`; unknown avg `8.453` n `789`
- 24h: commodity avg `0.4026` n `12`; crypto_alt avg `-0.903` n `233`; crypto_major avg `-0.2722` n `8`; equity avg `-0.6205` n `134`; fx avg `-0.0487` n `6`; index avg `-0.2341` n `26`; metal avg `0.4325` n `20`; unknown avg `7.2605` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
