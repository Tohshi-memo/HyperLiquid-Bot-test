# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T09:07:23.721071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `2.19` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.11` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.7564` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `1.2487` n `239`; crypto_major avg `1.4398` n `8`; equity avg `0.4135` n `162`; fx avg `-0.0019` n `6`; index avg `0.0525` n `27`; metal avg `0.0646` n `20`; unknown avg `0.8677` n `1257`
- 1h: commodity avg `0.0261` n `13`; crypto_alt avg `1.4141` n `239`; crypto_major avg `2.2161` n `8`; equity avg `0.4597` n `162`; fx avg `-0.0154` n `6`; index avg `0.0494` n `27`; metal avg `0.1061` n `20`; unknown avg `1.01` n `1259`
- 4h: commodity avg `-0.0328` n `13`; crypto_alt avg `0.4907` n `239`; crypto_major avg `0.9263` n `8`; equity avg `0.2257` n `162`; fx avg `-0.0135` n `6`; index avg `0.033` n `27`; metal avg `0.1557` n `20`; unknown avg `1.016` n `1223`
- 24h: commodity avg `0.0162` n `13`; crypto_alt avg `-4.298` n `239`; crypto_major avg `-3.1206` n `8`; equity avg `-0.6302` n `162`; fx avg `0.0303` n `6`; index avg `-0.0464` n `27`; metal avg `-0.33` n `20`; unknown avg `46.5567` n `1076`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
