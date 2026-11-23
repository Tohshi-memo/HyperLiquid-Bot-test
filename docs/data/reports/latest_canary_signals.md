# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T16:07:28.843937+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9758` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.814` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6565` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.2138` n `239`; crypto_major avg `-0.0362` n `8`; equity avg `0.0218` n `166`; fx avg `0.0135` n `6`; index avg `0.0202` n `27`; metal avg `-0.0201` n `20`; unknown avg `0.0312` n `1252`
- 1h: commodity avg `-0.3535` n `13`; crypto_alt avg `-0.5277` n `239`; crypto_major avg `-0.7942` n `8`; equity avg `0.0472` n `166`; fx avg `-0.0265` n `6`; index avg `-0.0109` n `27`; metal avg `-0.1327` n `20`; unknown avg `106.0109` n `1256`
- 4h: commodity avg `-0.7465` n `13`; crypto_alt avg `2.5697` n `239`; crypto_major avg `3.2293` n `8`; equity avg `4.8858` n `166`; fx avg `-0.1751` n `6`; index avg `0.5399` n `27`; metal avg `0.4153` n `20`; unknown avg `108.456` n `1250`
- 24h: commodity avg `-1.6508` n `13`; crypto_alt avg `3.3881` n `239`; crypto_major avg `4.3071` n `8`; equity avg `6.8966` n `166`; fx avg `-0.0181` n `6`; index avg `0.6243` n `27`; metal avg `0.7602` n `20`; unknown avg `245.615` n `1061`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
