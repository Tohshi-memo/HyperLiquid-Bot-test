# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T13:52:31.002516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4549` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.0381` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.8168` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0476` n `12`; crypto_alt avg `-0.2565` n `230`; crypto_major avg `-0.2169` n `8`; equity avg `-0.0197` n `92`; fx avg `0.0103` n `6`; index avg `0.0007` n `25`; metal avg `0.0246` n `20`; unknown avg `0.0323` n `766`
- 1h: commodity avg `-0.1289` n `12`; crypto_alt avg `0.3381` n `230`; crypto_major avg `0.46` n `8`; equity avg `-0.3409` n `92`; fx avg `-0.0016` n `6`; index avg `0.0367` n `25`; metal avg `0.1931` n `20`; unknown avg `-0.232` n `766`
- 4h: commodity avg `-0.1761` n `12`; crypto_alt avg `1.5711` n `230`; crypto_major avg `2.2788` n `8`; equity avg `0.2407` n `92`; fx avg `0.0009` n `6`; index avg `0.2504` n `25`; metal avg `0.462` n `20`; unknown avg `0.9943` n `766`
- 24h: commodity avg `1.278` n `12`; crypto_alt avg `1.103` n `230`; crypto_major avg `2.5368` n `8`; equity avg `0.5274` n `92`; fx avg `-0.0198` n `6`; index avg `0.2054` n `25`; metal avg `0.4129` n `20`; unknown avg `-0.0283` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
