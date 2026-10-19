# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T01:07:29.121843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0577` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.377` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0533` n `13`; crypto_alt avg `-0.037` n `237`; crypto_major avg `-0.033` n `8`; equity avg `0.1309` n `151`; fx avg `0.0068` n `6`; index avg `0.0196` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.1024` n `1192`
- 1h: commodity avg `0.0683` n `13`; crypto_alt avg `0.1734` n `237`; crypto_major avg `0.2075` n `8`; equity avg `0.1466` n `151`; fx avg `0.0024` n `6`; index avg `-0.0337` n `26`; metal avg `-0.0629` n `20`; unknown avg `-0.1429` n `1136`
- 4h: commodity avg `-0.4184` n `13`; crypto_alt avg `3.4086` n `237`; crypto_major avg `2.6393` n `8`; equity avg `2.5696` n `151`; fx avg `0.0581` n `6`; index avg `0.4469` n `26`; metal avg `0.2623` n `20`; unknown avg `4.7334` n `1046`
- 24h: commodity avg `-0.3027` n `13`; crypto_alt avg `-0.7655` n `237`; crypto_major avg `0.5219` n `8`; equity avg `1.8686` n `151`; fx avg `0.0033` n `6`; index avg `0.3459` n `26`; metal avg `0.1933` n `20`; unknown avg `1.5295` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2048`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0827`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
