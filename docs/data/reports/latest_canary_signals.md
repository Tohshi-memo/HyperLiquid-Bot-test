# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T02:37:38.964133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.8551` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.8149` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.316` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.2481` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_equity_divergence: score `3.238` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `2.813` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.0826` n `239`; crypto_major avg `0.4075` n `8`; equity avg `0.0841` n `162`; fx avg `0.0006` n `6`; index avg `0.0071` n `27`; metal avg `0.0151` n `20`; unknown avg `0.0126` n `1263`
- 1h: commodity avg `0.0327` n `13`; crypto_alt avg `2.7497` n `239`; crypto_major avg `3.8878` n `8`; equity avg `0.6498` n `162`; fx avg `0.0018` n `6`; index avg `0.0289` n `27`; metal avg `0.0729` n `20`; unknown avg `24.3078` n `1256`
- 4h: commodity avg `0.071` n `13`; crypto_alt avg `3.0088` n `239`; crypto_major avg `3.3191` n `8`; equity avg `0.5061` n `162`; fx avg `0.0065` n `6`; index avg `0.0199` n `27`; metal avg `0.0031` n `20`; unknown avg `1.4388` n `1220`
- 24h: commodity avg `0.0246` n `13`; crypto_alt avg `-5.6828` n `239`; crypto_major avg `-4.7786` n `8`; equity avg `-0.8698` n `162`; fx avg `0.0331` n `6`; index avg `-0.0792` n `27`; metal avg `-0.4486` n `20`; unknown avg `46.8751` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
