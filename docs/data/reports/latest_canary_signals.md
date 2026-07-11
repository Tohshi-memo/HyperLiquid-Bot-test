# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T01:22:29.244876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.185` n `229`; crypto_major avg `0.2153` n `8`; equity avg `0.0229` n `92`; fx avg `0.0028` n `6`; index avg `0.0022` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.1572` n `765`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.3079` n `229`; crypto_major avg `0.2751` n `8`; equity avg `0.0389` n `92`; fx avg `0.0016` n `6`; index avg `0.0035` n `25`; metal avg `-0.002` n `20`; unknown avg `1.1313` n `765`
- 4h: commodity avg `0.0596` n `12`; crypto_alt avg `0.3214` n `229`; crypto_major avg `0.274` n `8`; equity avg `0.102` n `92`; fx avg `0.0017` n `6`; index avg `-0.0173` n `25`; metal avg `0.001` n `20`; unknown avg `2.562` n `765`
- 24h: commodity avg `-0.2874` n `12`; crypto_alt avg `1.0563` n `229`; crypto_major avg `0.959` n `8`; equity avg `-0.5469` n `92`; fx avg `-0.1695` n `6`; index avg `0.087` n `25`; metal avg `0.0766` n `20`; unknown avg `3.4036` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
