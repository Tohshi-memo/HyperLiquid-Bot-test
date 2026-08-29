# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T23:07:26.548076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `12`; crypto_alt avg `0.0285` n `231`; crypto_major avg `0.0626` n `8`; equity avg `0.0008` n `128`; fx avg `0.0031` n `6`; index avg `-0.0245` n `26`; metal avg `0.0052` n `20`; unknown avg `-0.0645` n `793`
- 1h: commodity avg `0.0026` n `12`; crypto_alt avg `0.0845` n `231`; crypto_major avg `0.1356` n `8`; equity avg `0.008` n `128`; fx avg `0.0002` n `6`; index avg `0.0039` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.2782` n `779`
- 4h: commodity avg `-0.012` n `12`; crypto_alt avg `-0.0619` n `231`; crypto_major avg `-0.0089` n `8`; equity avg `0.1611` n `128`; fx avg `0.0035` n `6`; index avg `0.0197` n `26`; metal avg `0.0023` n `20`; unknown avg `0.0283` n `774`
- 24h: commodity avg `0.0502` n `12`; crypto_alt avg `0.5322` n `231`; crypto_major avg `0.8941` n `8`; equity avg `0.4231` n `128`; fx avg `-0.0272` n `6`; index avg `0.0853` n `26`; metal avg `0.1145` n `20`; unknown avg `-0.0207` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
