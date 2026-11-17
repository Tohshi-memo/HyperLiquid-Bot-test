# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T23:07:26.142822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1973` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9549` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `0.4039` n `239`; crypto_major avg `0.677` n `8`; equity avg `0.6951` n `163`; fx avg `-0.0128` n `6`; index avg `0.0748` n `27`; metal avg `0.0554` n `20`; unknown avg `0.8445` n `1259`
- 1h: commodity avg `0.0086` n `13`; crypto_alt avg `0.8836` n `239`; crypto_major avg `1.1181` n `8`; equity avg `1.6749` n `163`; fx avg `0.0121` n `6`; index avg `0.1704` n `27`; metal avg `0.0753` n `20`; unknown avg `4.1154` n `1223`
- 4h: commodity avg `-0.1617` n `13`; crypto_alt avg `2.0308` n `239`; crypto_major avg `2.0356` n `8`; equity avg `3.1893` n `163`; fx avg `-0.0347` n `6`; index avg `0.3135` n `27`; metal avg `0.0807` n `20`; unknown avg `4.0508` n `1191`
- 24h: commodity avg `0.2688` n `13`; crypto_alt avg `1.1026` n `239`; crypto_major avg `1.0068` n `8`; equity avg `1.7879` n `163`; fx avg `0.0201` n `6`; index avg `0.1509` n `27`; metal avg `0.0446` n `20`; unknown avg `6.8536` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1714`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
