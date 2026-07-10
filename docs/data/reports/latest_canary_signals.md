# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T23:52:24.324185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `12`; crypto_alt avg `-0.0435` n `229`; crypto_major avg `-0.0335` n `8`; equity avg `0.0433` n `92`; fx avg `0.0006` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.0362` n `765`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.0389` n `229`; crypto_major avg `-0.0189` n `8`; equity avg `0.07` n `92`; fx avg `0.0283` n `6`; index avg `-0.0131` n `25`; metal avg `0.0052` n `20`; unknown avg `0.187` n `765`
- 4h: commodity avg `-0.0276` n `12`; crypto_alt avg `0.2851` n `229`; crypto_major avg `0.0064` n `8`; equity avg `0.0563` n `92`; fx avg `-0.0094` n `6`; index avg `-0.0008` n `25`; metal avg `0.0716` n `20`; unknown avg `-0.4437` n `765`
- 24h: commodity avg `-0.2615` n `12`; crypto_alt avg `1.1894` n `229`; crypto_major avg `1.0578` n `8`; equity avg `-0.737` n `92`; fx avg `-0.171` n `6`; index avg `0.009` n `25`; metal avg `0.1405` n `20`; unknown avg `-0.2979` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
