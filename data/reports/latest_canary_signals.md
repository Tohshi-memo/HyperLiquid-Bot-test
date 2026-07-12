# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T22:52:26.345806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `-0.0714` n `230`; crypto_major avg `-0.0366` n `8`; equity avg `0.0011` n `92`; fx avg `-0.0032` n `6`; index avg `-0.0025` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0396` n `765`
- 1h: commodity avg `-0.167` n `12`; crypto_alt avg `-0.6865` n `230`; crypto_major avg `-0.5994` n `8`; equity avg `-0.3188` n `92`; fx avg `-0.0238` n `6`; index avg `-0.0795` n `25`; metal avg `-0.1981` n `20`; unknown avg `0.0971` n `765`
- 4h: commodity avg `-0.1909` n `12`; crypto_alt avg `-0.9983` n `230`; crypto_major avg `-1.0587` n `8`; equity avg `-0.2942` n `92`; fx avg `-0.0518` n `6`; index avg `-0.0803` n `25`; metal avg `-0.2197` n `20`; unknown avg `0.2709` n `765`
- 24h: commodity avg `0.1627` n `12`; crypto_alt avg `-1.7528` n `230`; crypto_major avg `-1.1967` n `8`; equity avg `-0.4527` n `92`; fx avg `-0.0629` n `6`; index avg `-0.1559` n `25`; metal avg `-0.321` n `20`; unknown avg `0.3642` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
