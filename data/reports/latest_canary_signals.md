# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T03:37:30.103413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `12`; crypto_alt avg `0.1621` n `233`; crypto_major avg `0.1451` n `8`; equity avg `-0.0338` n `136`; fx avg `-0.0026` n `6`; index avg `-0.0127` n `27`; metal avg `-0.0083` n `20`; unknown avg `0.2227` n `908`
- 1h: commodity avg `-0.0211` n `12`; crypto_alt avg `-0.3425` n `233`; crypto_major avg `-0.2707` n `8`; equity avg `-0.2329` n `136`; fx avg `-0.0089` n `6`; index avg `-0.0327` n `27`; metal avg `0.036` n `20`; unknown avg `0.1868` n `902`
- 4h: commodity avg `0.0871` n `12`; crypto_alt avg `-0.4654` n `233`; crypto_major avg `-0.3326` n `8`; equity avg `0.0577` n `136`; fx avg `0.0838` n `6`; index avg `0.0661` n `27`; metal avg `0.1591` n `20`; unknown avg `0.0259` n `896`
- 24h: commodity avg `-0.0751` n `12`; crypto_alt avg `-0.7577` n `233`; crypto_major avg `0.3336` n `8`; equity avg `-0.1586` n `136`; fx avg `0.1001` n `6`; index avg `-0.0283` n `27`; metal avg `-0.2128` n `20`; unknown avg `5.3618` n `790`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
