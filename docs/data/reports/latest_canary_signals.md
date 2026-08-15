# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T00:22:29.153309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.072` n `230`; crypto_major avg `-0.0142` n `8`; equity avg `0.0041` n `114`; fx avg `0.0012` n `6`; index avg `0.0002` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.0042` n `791`
- 1h: commodity avg `0.0796` n `12`; crypto_alt avg `0.2187` n `230`; crypto_major avg `0.1807` n `8`; equity avg `-0.0779` n `114`; fx avg `-0.0225` n `6`; index avg `-0.0059` n `25`; metal avg `0.039` n `20`; unknown avg `0.0923` n `791`
- 4h: commodity avg `0.1291` n `12`; crypto_alt avg `0.4246` n `230`; crypto_major avg `0.2999` n `8`; equity avg `0.0022` n `114`; fx avg `-0.0304` n `6`; index avg `-0.0075` n `25`; metal avg `0.0879` n `20`; unknown avg `2.6304` n `791`
- 24h: commodity avg `0.2783` n `12`; crypto_alt avg `0.1223` n `230`; crypto_major avg `-0.7426` n `8`; equity avg `-0.4766` n `114`; fx avg `0.0643` n `6`; index avg `-0.1002` n `25`; metal avg `0.314` n `20`; unknown avg `-0.2887` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
