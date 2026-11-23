# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T14:52:33.302140+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.7253` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `3.6683` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.0546` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.0193` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.121` n `13`; crypto_alt avg `-1.0199` n `239`; crypto_major avg `-1.569` n `8`; equity avg `-1.8779` n `166`; fx avg `-0.0162` n `6`; index avg `-0.0942` n `27`; metal avg `-0.0765` n `20`; unknown avg `3.8764` n `1266`
- 1h: commodity avg `0.1576` n `13`; crypto_alt avg `3.4498` n `239`; crypto_major avg `3.8259` n `8`; equity avg `3.7723` n `166`; fx avg `-0.0168` n `6`; index avg `0.5133` n `27`; metal avg `0.7713` n `20`; unknown avg `128.3137` n `1260`
- 4h: commodity avg `-0.226` n `13`; crypto_alt avg `2.9887` n `239`; crypto_major avg `3.4993` n `8`; equity avg `2.8417` n `166`; fx avg `-0.152` n `6`; index avg `0.3653` n `27`; metal avg `0.48` n `20`; unknown avg `13.0772` n `1252`
- 24h: commodity avg `-1.091` n `13`; crypto_alt avg `3.9104` n `239`; crypto_major avg `4.8288` n `8`; equity avg `5.1665` n `166`; fx avg `0.0394` n `6`; index avg `0.49` n `27`; metal avg `0.9069` n `20`; unknown avg `13.1067` n `1059`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
