# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T03:52:28.414494+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.7886` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.7778` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.7158` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.2652` n `230`; crypto_major avg `-0.0137` n `8`; equity avg `-0.0126` n `121`; fx avg `0.0085` n `6`; index avg `0.0065` n `25`; metal avg `-0.008` n `20`; unknown avg `0.136` n `794`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `1.3413` n `230`; crypto_major avg `1.1201` n `8`; equity avg `-0.0024` n `121`; fx avg `0.0122` n `6`; index avg `0.0131` n `25`; metal avg `0.0037` n `20`; unknown avg `0.1747` n `793`
- 4h: commodity avg `-0.0181` n `12`; crypto_alt avg `4.2206` n `230`; crypto_major avg `3.7597` n `8`; equity avg `0.0439` n `121`; fx avg `0.0348` n `6`; index avg `0.0134` n `25`; metal avg `-0.0289` n `20`; unknown avg `0.3468` n `793`
- 24h: commodity avg `0.0747` n `12`; crypto_alt avg `11.8659` n `230`; crypto_major avg `9.9253` n `8`; equity avg `0.3397` n `121`; fx avg `0.045` n `6`; index avg `0.0324` n `25`; metal avg `0.2507` n `20`; unknown avg `1.6002` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
