# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T02:22:28.548583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.2139` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.1333` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.6584` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.9004` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5974` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `1.315` n `239`; crypto_major avg `1.5116` n `8`; equity avg `0.2975` n `162`; fx avg `0.0062` n `6`; index avg `0.02` n `27`; metal avg `0.0436` n `20`; unknown avg `0.5193` n `1261`
- 1h: commodity avg `0.0256` n `13`; crypto_alt avg `2.4297` n `239`; crypto_major avg `3.2395` n `8`; equity avg `0.5811` n `162`; fx avg `0.0007` n `6`; index avg `0.0289` n `27`; metal avg `0.1062` n `20`; unknown avg `47.5296` n `1258`
- 4h: commodity avg `0.0767` n `13`; crypto_alt avg `2.1584` n `239`; crypto_major avg `1.8737` n `8`; equity avg `0.2763` n `162`; fx avg `0.0076` n `6`; index avg `0.0015` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.9643` n `1220`
- 24h: commodity avg `0.0276` n `13`; crypto_alt avg `-5.7679` n `239`; crypto_major avg `-5.4021` n `8`; equity avg `-0.9763` n `162`; fx avg `0.0327` n `6`; index avg `-0.0907` n `27`; metal avg `-0.4975` n `20`; unknown avg `47.2972` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
