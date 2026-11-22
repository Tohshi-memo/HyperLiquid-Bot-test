# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T11:22:31.534984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2991` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2328` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0767` n `239`; crypto_major avg `-0.0089` n `8`; equity avg `0.0294` n `166`; fx avg `-0.0011` n `6`; index avg `-0.0141` n `27`; metal avg `-0.0036` n `20`; unknown avg `0.0837` n `1261`
- 1h: commodity avg `0.005` n `13`; crypto_alt avg `0.2345` n `239`; crypto_major avg `0.0612` n `8`; equity avg `0.1003` n `166`; fx avg `-0.0085` n `6`; index avg `-0.0146` n `27`; metal avg `0.0269` n `20`; unknown avg `365.7734` n `1257`
- 4h: commodity avg `0.0795` n `13`; crypto_alt avg `2.2281` n `239`; crypto_major avg `2.3786` n `8`; equity avg `1.2179` n `166`; fx avg `-0.0202` n `6`; index avg `0.1085` n `27`; metal avg `0.1458` n `20`; unknown avg `220.6635` n `1141`
- 24h: commodity avg `0.0686` n `13`; crypto_alt avg `3.5504` n `239`; crypto_major avg `4.1535` n `8`; equity avg `1.8986` n `166`; fx avg `-0.0062` n `6`; index avg `0.2189` n `27`; metal avg `0.174` n `20`; unknown avg `0.1942` n `1056`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
