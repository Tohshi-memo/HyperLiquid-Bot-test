# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T19:07:34.764190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.2663` n `234`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0016` n `141`; fx avg `-0.0035` n `6`; index avg `0.0169` n `26`; metal avg `0.0895` n `20`; unknown avg `2.6655` n `941`
- 1h: commodity avg `0.1512` n `12`; crypto_alt avg `-0.4038` n `234`; crypto_major avg `0.1064` n `8`; equity avg `-0.004` n `141`; fx avg `-0.0088` n `6`; index avg `0.0067` n `26`; metal avg `0.0616` n `20`; unknown avg `4.1105` n `941`
- 4h: commodity avg `0.232` n `12`; crypto_alt avg `-1.8483` n `234`; crypto_major avg `-0.9892` n `8`; equity avg `-0.3193` n `141`; fx avg `-0.0243` n `6`; index avg `-0.0599` n `26`; metal avg `0.0186` n `20`; unknown avg `3.0983` n `919`
- 24h: commodity avg `0.4626` n `12`; crypto_alt avg `-3.1753` n `234`; crypto_major avg `-3.602` n `8`; equity avg `-1.2919` n `140`; fx avg `-0.0183` n `6`; index avg `-0.3281` n `26`; metal avg `-0.7321` n `20`; unknown avg `13.571` n `878`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.2239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2042`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
