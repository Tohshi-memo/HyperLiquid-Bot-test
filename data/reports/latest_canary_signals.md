# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T10:37:27.495767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5324` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2915` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1221` n `12`; crypto_alt avg `0.003` n `234`; crypto_major avg `-0.049` n `8`; equity avg `0.0266` n `140`; fx avg `-0.0046` n `6`; index avg `0.0128` n `26`; metal avg `-0.0349` n `20`; unknown avg `-0.0886` n `944`
- 1h: commodity avg `-0.2865` n `12`; crypto_alt avg `-0.3607` n `234`; crypto_major avg `-0.6768` n `8`; equity avg `0.0169` n `140`; fx avg `-0.0182` n `6`; index avg `0.018` n `26`; metal avg `-0.0045` n `20`; unknown avg `3.0018` n `940`
- 4h: commodity avg `-0.2193` n `12`; crypto_alt avg `1.7016` n `234`; crypto_major avg `2.3131` n `8`; equity avg `0.837` n `140`; fx avg `-0.044` n `6`; index avg `0.1067` n `26`; metal avg `0.0216` n `20`; unknown avg `1.7827` n `920`
- 24h: commodity avg `-0.8667` n `12`; crypto_alt avg `6.8306` n `234`; crypto_major avg `5.5326` n `8`; equity avg `2.0975` n `140`; fx avg `-0.107` n `6`; index avg `0.3697` n `26`; metal avg `-0.0013` n `20`; unknown avg `9.1003` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
