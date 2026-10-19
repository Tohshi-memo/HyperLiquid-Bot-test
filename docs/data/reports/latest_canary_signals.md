# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T09:37:26.448392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `13`; crypto_alt avg `0.0321` n `237`; crypto_major avg `0.0938` n `8`; equity avg `0.0246` n `151`; fx avg `0.0052` n `6`; index avg `-0.0038` n `26`; metal avg `0.0069` n `20`; unknown avg `-0.0759` n `1195`
- 1h: commodity avg `0.2367` n `13`; crypto_alt avg `-0.0189` n `237`; crypto_major avg `0.1333` n `8`; equity avg `-0.0571` n `151`; fx avg `0.0068` n `6`; index avg `-0.0243` n `26`; metal avg `0.0273` n `20`; unknown avg `0.052` n `1193`
- 4h: commodity avg `0.2223` n `13`; crypto_alt avg `0.263` n `237`; crypto_major avg `0.3155` n `8`; equity avg `0.0333` n `151`; fx avg `-0.0113` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0731` n `20`; unknown avg `0.4953` n `1126`
- 24h: commodity avg `-0.216` n `13`; crypto_alt avg `0.125` n `237`; crypto_major avg `0.9535` n `8`; equity avg `2.3072` n `151`; fx avg `-0.0479` n `6`; index avg `0.4254` n `26`; metal avg `0.2283` n `20`; unknown avg `1.0645` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1981`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1442`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1284`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.061`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
