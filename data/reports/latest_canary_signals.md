# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T12:07:29.369066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.063` n `235`; crypto_major avg `0.1401` n `8`; equity avg `0.0273` n `143`; fx avg `-0.0006` n `6`; index avg `0.0015` n `26`; metal avg `0.0023` n `20`; unknown avg `0.0324` n `1071`
- 1h: commodity avg `0.0252` n `13`; crypto_alt avg `0.0081` n `235`; crypto_major avg `0.089` n `8`; equity avg `0.023` n `143`; fx avg `0.0069` n `6`; index avg `0.0006` n `26`; metal avg `0.0057` n `20`; unknown avg `-0.178` n `1071`
- 4h: commodity avg `0.042` n `13`; crypto_alt avg `-0.3257` n `235`; crypto_major avg `0.2217` n `8`; equity avg `0.0624` n `143`; fx avg `0.0279` n `6`; index avg `0.0143` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.0975` n `1071`
- 24h: commodity avg `0.181` n `13`; crypto_alt avg `1.5719` n `235`; crypto_major avg `1.2743` n `8`; equity avg `0.2702` n `143`; fx avg `0.0052` n `6`; index avg `0.0403` n `26`; metal avg `0.0069` n `20`; unknown avg `0.0095` n `902`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
