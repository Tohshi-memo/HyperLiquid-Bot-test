# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T03:22:29.855161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.7019` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.6739` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.9523` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0067` n `13`; crypto_alt avg `0.1457` n `239`; crypto_major avg `0.1727` n `8`; equity avg `0.0406` n `162`; fx avg `-0.0021` n `6`; index avg `0.0029` n `27`; metal avg `0.0123` n `20`; unknown avg `0.7162` n `1261`
- 1h: commodity avg `-0.0105` n `13`; crypto_alt avg `0.7339` n `239`; crypto_major avg `1.3257` n `8`; equity avg `0.2981` n `162`; fx avg `-0.0006` n `6`; index avg `0.0145` n `27`; metal avg `0.0927` n `20`; unknown avg `0.3458` n `1261`
- 4h: commodity avg `0.0387` n `13`; crypto_alt avg `3.2566` n `239`; crypto_major avg `3.7126` n `8`; equity avg `0.7603` n `162`; fx avg `-0.004` n `6`; index avg `0.025` n `27`; metal avg `0.0107` n `20`; unknown avg `2.6342` n `1252`
- 24h: commodity avg `0.01` n `13`; crypto_alt avg `-5.3813` n `239`; crypto_major avg `-3.9958` n `8`; equity avg `-0.7187` n `162`; fx avg `0.0401` n `6`; index avg `-0.0688` n `27`; metal avg `-0.3934` n `20`; unknown avg `47.6282` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
