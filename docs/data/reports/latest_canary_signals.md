# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T11:07:26.217345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0146` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8331` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.599` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1144` n `239`; crypto_major avg `0.0921` n `8`; equity avg `-0.0051` n `162`; fx avg `0.0023` n `6`; index avg `-0.0011` n `27`; metal avg `0.0127` n `20`; unknown avg `0.5573` n `1257`
- 1h: commodity avg `0.0016` n `13`; crypto_alt avg `-0.0192` n `239`; crypto_major avg `0.0061` n `8`; equity avg `-0.0032` n `162`; fx avg `-0.0051` n `6`; index avg `0.0005` n `27`; metal avg `-0.0026` n `20`; unknown avg `0.7534` n `1261`
- 4h: commodity avg `-0.0659` n `13`; crypto_alt avg `0.971` n `239`; crypto_major avg `1.9487` n `8`; equity avg `0.3497` n `162`; fx avg `-0.023` n `6`; index avg `0.0424` n `27`; metal avg `0.1156` n `20`; unknown avg `0.9998` n `1245`
- 24h: commodity avg `0.005` n `13`; crypto_alt avg `-3.8349` n `239`; crypto_major avg `-3.0245` n `8`; equity avg `-0.7135` n `162`; fx avg `0.0281` n `6`; index avg `-0.0555` n `27`; metal avg `-0.3391` n `20`; unknown avg `-0.5263` n `1136`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
