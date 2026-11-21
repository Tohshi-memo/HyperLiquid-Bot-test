# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T13:52:28.958192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.6377` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.5118` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.6189` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.17` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.0547` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0137` n `13`; crypto_alt avg `0.2609` n `239`; crypto_major avg `0.3496` n `8`; equity avg `0.1907` n `166`; fx avg `0.0017` n `6`; index avg `0.0232` n `27`; metal avg `-0.0143` n `20`; unknown avg `158.6472` n `1262`
- 1h: commodity avg `0.0129` n `13`; crypto_alt avg `1.7183` n `239`; crypto_major avg `2.1829` n `8`; equity avg `0.9138` n `166`; fx avg `0.0126` n `6`; index avg `0.0947` n `27`; metal avg `0.1282` n `20`; unknown avg `1.526` n `1256`
- 4h: commodity avg `0.0676` n `13`; crypto_alt avg `2.3626` n `239`; crypto_major avg `3.7053` n `8`; equity avg `1.0864` n `166`; fx avg `0.0357` n `6`; index avg `0.1187` n `27`; metal avg `0.1935` n `20`; unknown avg `326.5888` n `1226`
- 24h: commodity avg `0.3461` n `13`; crypto_alt avg `-2.1124` n `239`; crypto_major avg `-2.0091` n `8`; equity avg `-2.9506` n `166`; fx avg `-0.1187` n `6`; index avg `-0.3184` n `27`; metal avg `-0.2056` n `20`; unknown avg `0.1413` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
