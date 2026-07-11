# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T04:52:27.391837+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0113` n `12`; crypto_alt avg `-0.2167` n `229`; crypto_major avg `-0.1374` n `8`; equity avg `0.0197` n `92`; fx avg `0.0001` n `6`; index avg `-0.0017` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0265` n `765`
- 1h: commodity avg `-0.041` n `12`; crypto_alt avg `-0.2779` n `229`; crypto_major avg `-0.1666` n `8`; equity avg `-0.0306` n `92`; fx avg `-0.0013` n `6`; index avg `0.0043` n `25`; metal avg `0.0055` n `20`; unknown avg `0.1418` n `765`
- 4h: commodity avg `-0.0882` n `12`; crypto_alt avg `-0.0714` n `229`; crypto_major avg `-0.1221` n `8`; equity avg `0.0134` n `92`; fx avg `0.0029` n `6`; index avg `0.0108` n `25`; metal avg `0.0201` n `20`; unknown avg `-0.1807` n `763`
- 24h: commodity avg `-0.3285` n `12`; crypto_alt avg `0.1801` n `229`; crypto_major avg `-0.4544` n `8`; equity avg `-0.7591` n `92`; fx avg `-0.1928` n `6`; index avg `0.0461` n `25`; metal avg `-0.0034` n `20`; unknown avg `4.1751` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
