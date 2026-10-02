# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T22:22:31.603724+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.026` n `13`; crypto_alt avg `-0.1987` n `235`; crypto_major avg `0.0371` n `8`; equity avg `0.0257` n `143`; fx avg `-0.0034` n `6`; index avg `0.0656` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.1877` n `984`
- 1h: commodity avg `0.05` n `13`; crypto_alt avg `0.0853` n `235`; crypto_major avg `0.0973` n `8`; equity avg `0.0074` n `143`; fx avg `-0.0705` n `6`; index avg `0.0007` n `26`; metal avg `0.0106` n `20`; unknown avg `-0.0813` n `966`
- 4h: commodity avg `0.2323` n `13`; crypto_alt avg `-1.3591` n `235`; crypto_major avg `-0.8439` n `8`; equity avg `0.1314` n `143`; fx avg `-0.0278` n `6`; index avg `0.0349` n `26`; metal avg `0.1101` n `20`; unknown avg `-0.5453` n `906`
- 24h: commodity avg `0.067` n `13`; crypto_alt avg `-1.2416` n `235`; crypto_major avg `-0.8082` n `8`; equity avg `0.77` n `142`; fx avg `-0.1576` n `6`; index avg `0.3046` n `26`; metal avg `-0.2037` n `20`; unknown avg `-0.4753` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
