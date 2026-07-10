# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T20:58:37.023627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `-0.0974` n `229`; crypto_major avg `-0.0942` n `8`; equity avg `0.0316` n `92`; fx avg `0.0034` n `6`; index avg `0.0023` n `25`; metal avg `0.0364` n `20`; unknown avg `-0.1427` n `765`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `-0.1886` n `229`; crypto_major avg `-0.2153` n `8`; equity avg `-0.0158` n `92`; fx avg `-0.0159` n `6`; index avg `0.0183` n `25`; metal avg `0.0789` n `20`; unknown avg `-0.2863` n `765`
- 4h: commodity avg `0.1426` n `12`; crypto_alt avg `-0.2962` n `229`; crypto_major avg `-0.3187` n `8`; equity avg `-0.2529` n `92`; fx avg `-0.0439` n `6`; index avg `0.0169` n `25`; metal avg `0.0659` n `20`; unknown avg `-0.3291` n `765`
- 24h: commodity avg `-0.2167` n `12`; crypto_alt avg `0.4659` n `229`; crypto_major avg `0.6731` n `8`; equity avg `-0.6423` n `92`; fx avg `-0.163` n `6`; index avg `0.0597` n `25`; metal avg `0.1641` n `20`; unknown avg `-0.2255` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
