# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T01:07:31.412289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.457` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4104` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3643` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.4489` n `230`; crypto_major avg `0.6037` n `8`; equity avg `-0.0262` n `121`; fx avg `0.004` n `6`; index avg `-0.0035` n `25`; metal avg `0.0013` n `20`; unknown avg `0.6409` n `793`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `1.405` n `230`; crypto_major avg `1.2501` n `8`; equity avg `0.0134` n `121`; fx avg `0.0049` n `6`; index avg `-0.004` n `25`; metal avg `-0.008` n `20`; unknown avg `0.4825` n `793`
- 4h: commodity avg `-0.0601` n `12`; crypto_alt avg `2.417` n `230`; crypto_major avg `2.3969` n `8`; equity avg `0.0326` n `121`; fx avg `0.0043` n `6`; index avg `0.0286` n `25`; metal avg `-0.0135` n `20`; unknown avg `0.5612` n `793`
- 24h: commodity avg `0.0626` n `12`; crypto_alt avg `9.446` n `230`; crypto_major avg `7.1417` n `8`; equity avg `0.742` n `121`; fx avg `-0.0312` n `6`; index avg `0.1177` n `25`; metal avg `0.4223` n `20`; unknown avg `1.8268` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
