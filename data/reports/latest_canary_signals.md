# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T00:22:22.774364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.6929` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.6704` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.5787` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0135` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `0.6729` n `230`; crypto_major avg `0.7975` n `8`; equity avg `0.063` n `121`; fx avg `0.0005` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0613` n `793`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.029` n `230`; crypto_major avg `-1.0101` n `8`; equity avg `0.0641` n `121`; fx avg `0.0004` n `6`; index avg `0.0034` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.3352` n `793`
- 4h: commodity avg `0.0036` n `12`; crypto_alt avg `2.3826` n `230`; crypto_major avg `2.674` n `8`; equity avg `0.0953` n `121`; fx avg `-0.0017` n `6`; index avg `0.0275` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.056` n `793`
- 24h: commodity avg `0.1798` n `12`; crypto_alt avg `8.3256` n `230`; crypto_major avg `6.6238` n `8`; equity avg `0.8019` n `121`; fx avg `-0.0139` n `6`; index avg `0.1034` n `25`; metal avg `0.4614` n `20`; unknown avg `1.2434` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
