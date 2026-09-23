# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T05:52:31.922909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.5181` n `234`; crypto_major avg `-0.3373` n `8`; equity avg `0.0291` n `140`; fx avg `0.0075` n `6`; index avg `0.0098` n `26`; metal avg `-0.0193` n `20`; unknown avg `8.1016` n `945`
- 1h: commodity avg `0.1144` n `12`; crypto_alt avg `-0.4657` n `234`; crypto_major avg `-0.91` n `8`; equity avg `-0.1346` n `140`; fx avg `0.0502` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0912` n `20`; unknown avg `1.0582` n `943`
- 4h: commodity avg `-0.0972` n `12`; crypto_alt avg `0.9716` n `234`; crypto_major avg `0.561` n `8`; equity avg `0.0572` n `140`; fx avg `0.0497` n `6`; index avg `0.0254` n `26`; metal avg `-0.1115` n `20`; unknown avg `0.1221` n `937`
- 24h: commodity avg `-0.1469` n `12`; crypto_alt avg `3.4474` n `234`; crypto_major avg `1.7791` n `8`; equity avg `1.0744` n `140`; fx avg `-0.1477` n `6`; index avg `0.0995` n `26`; metal avg `0.1124` n `20`; unknown avg `2.6073` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
