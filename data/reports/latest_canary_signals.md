# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T23:37:26.851062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.7384` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.674` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.6457` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `-0.2917` n `230`; crypto_major avg `-0.5676` n `8`; equity avg `0.0166` n `121`; fx avg `-0.0016` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.1212` n `793`
- 1h: commodity avg `0.0004` n `12`; crypto_alt avg `0.0128` n `230`; crypto_major avg `0.0003` n `8`; equity avg `-0.0128` n `121`; fx avg `-0.0075` n `6`; index avg `0.0075` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.2217` n `793`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `2.9206` n `230`; crypto_major avg `3.7219` n `8`; equity avg `0.0762` n `121`; fx avg `-0.009` n `6`; index avg `0.0168` n `25`; metal avg `-0.0165` n `20`; unknown avg `-0.0578` n `793`
- 24h: commodity avg `0.1655` n `12`; crypto_alt avg `8.3612` n `230`; crypto_major avg `7.5954` n `8`; equity avg `0.981` n `121`; fx avg `-0.1033` n `6`; index avg `0.1418` n `25`; metal avg `0.4503` n `20`; unknown avg `1.399` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1721`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
