# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T07:37:31.189867+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.2582` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.1329` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `1.8279` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.6369` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `-0.1139` n `239`; crypto_major avg `-0.1256` n `8`; equity avg `-0.1011` n `166`; fx avg `-0.0069` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0204` n `20`; unknown avg `158.2499` n `1262`
- 1h: commodity avg `-0.0538` n `13`; crypto_alt avg `1.2969` n `239`; crypto_major avg `2.2044` n `8`; equity avg `0.5675` n `166`; fx avg `-0.0035` n `6`; index avg `0.0496` n `27`; metal avg `0.0715` n `20`; unknown avg `1.214` n `1256`
- 4h: commodity avg `-0.0236` n `13`; crypto_alt avg `0.9535` n `239`; crypto_major avg `1.9711` n `8`; equity avg `0.7251` n `166`; fx avg `-0.1011` n `6`; index avg `0.1093` n `27`; metal avg `0.1432` n `20`; unknown avg `4.1096` n `1216`
- 24h: commodity avg `0.4135` n `13`; crypto_alt avg `-5.5191` n `239`; crypto_major avg `-6.0416` n `8`; equity avg `-4.5858` n `166`; fx avg `-0.1338` n `6`; index avg `-0.4901` n `27`; metal avg `-0.1457` n `20`; unknown avg `17.0051` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
