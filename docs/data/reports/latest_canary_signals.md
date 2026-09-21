# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T09:52:27.416950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.575` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.436` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5299` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.056` n `12`; crypto_alt avg `-0.6655` n `234`; crypto_major avg `-0.7084` n `8`; equity avg `-0.0178` n `140`; fx avg `-0.0162` n `6`; index avg `0.0038` n `26`; metal avg `-0.0102` n `20`; unknown avg `2.869` n `942`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.1519` n `234`; crypto_major avg `0.1256` n `8`; equity avg `0.1143` n `140`; fx avg `0.008` n `6`; index avg `0.0087` n `26`; metal avg `-0.0452` n `20`; unknown avg `1.7147` n `940`
- 4h: commodity avg `-0.1258` n `12`; crypto_alt avg `1.8722` n `234`; crypto_major avg `2.4492` n `8`; equity avg `0.9193` n `140`; fx avg `-0.0802` n `6`; index avg `0.1316` n `26`; metal avg `0.0132` n `20`; unknown avg `2.4863` n `888`
- 24h: commodity avg `-0.6071` n `12`; crypto_alt avg `5.7694` n `234`; crypto_major avg `5.1686` n `8`; equity avg `2.0211` n `140`; fx avg `-0.0997` n `6`; index avg `0.3579` n `26`; metal avg `-0.0329` n `20`; unknown avg `7.8455` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
