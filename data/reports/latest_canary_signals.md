# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T05:52:17.193613+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.0506` n `228`; crypto_major avg `-0.0265` n `8`; equity avg `-0.0138` n `65`; fx avg `0.0` n `5`; index avg `-0.0061` n `23`; metal avg `-0.0116` n `18`; unknown avg `-0.3342` n `376`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.1983` n `228`; crypto_major avg `0.0244` n `8`; equity avg `0.0075` n `65`; fx avg `0.0189` n `5`; index avg `-0.0295` n `23`; metal avg `0.018` n `18`; unknown avg `-0.7505` n `375`
- 4h: commodity avg `0.1728` n `12`; crypto_alt avg `0.0094` n `228`; crypto_major avg `-0.0767` n `8`; equity avg `0.0111` n `65`; fx avg `-0.0004` n `5`; index avg `0.106` n `23`; metal avg `0.0461` n `18`; unknown avg `-0.8716` n `375`
- 24h: commodity avg `-0.1241` n `12`; crypto_alt avg `4.5402` n `228`; crypto_major avg `2.7424` n `8`; equity avg `3.5094` n `65`; fx avg `0.0385` n `5`; index avg `1.3095` n `23`; metal avg `-0.1153` n `18`; unknown avg `1.3919` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
