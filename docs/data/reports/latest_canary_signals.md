# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T05:37:37.933350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.985` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.978` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.3217` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0239` n `13`; crypto_alt avg `-0.3731` n `239`; crypto_major avg `-0.3861` n `8`; equity avg `-0.0605` n `162`; fx avg `0.0012` n `6`; index avg `0.0007` n `27`; metal avg `-0.0076` n `20`; unknown avg `0.4823` n `1263`
- 1h: commodity avg `0.007` n `13`; crypto_alt avg `-0.1566` n `239`; crypto_major avg `-0.4306` n `8`; equity avg `-0.0586` n `162`; fx avg `0.0041` n `6`; index avg `-0.0071` n `27`; metal avg `0.0156` n `20`; unknown avg `103.2511` n `1259`
- 4h: commodity avg `0.0684` n `13`; crypto_alt avg `2.9594` n `239`; crypto_major avg `4.0534` n `8`; equity avg `0.7317` n `162`; fx avg `0.0145` n `6`; index avg `0.025` n `27`; metal avg `0.0754` n `20`; unknown avg `88.6187` n `1240`
- 24h: commodity avg `0.0839` n `13`; crypto_alt avg `-5.4116` n `239`; crypto_major avg `-4.0805` n `8`; equity avg `-0.8051` n `162`; fx avg `0.0489` n `6`; index avg `-0.0799` n `27`; metal avg `-0.4487` n `20`; unknown avg `47.0332` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
