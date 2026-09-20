# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T03:37:29.405169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0307` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7229` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6814` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0443` n `12`; crypto_alt avg `-0.3998` n `234`; crypto_major avg `-0.2703` n `8`; equity avg `-0.0742` n `140`; fx avg `0.0008` n `6`; index avg `-0.0004` n `26`; metal avg `0.0091` n `20`; unknown avg `1.6697` n `943`
- 1h: commodity avg `0.0582` n `12`; crypto_alt avg `-1.2167` n `234`; crypto_major avg `-0.9439` n `8`; equity avg `-0.3947` n `140`; fx avg `0.0018` n `6`; index avg `-0.059` n `26`; metal avg `-0.0255` n `20`; unknown avg `6.046` n `941`
- 4h: commodity avg `0.2817` n `12`; crypto_alt avg `-1.5587` n `234`; crypto_major avg `-1.749` n `8`; equity avg `-0.3549` n `140`; fx avg `0.0192` n `6`; index avg `-0.0676` n `26`; metal avg `-0.0261` n `20`; unknown avg `6.6174` n `935`
- 24h: commodity avg `0.2272` n `12`; crypto_alt avg `-1.0664` n `234`; crypto_major avg `-2.1021` n `8`; equity avg `-0.2809` n `140`; fx avg `-0.0594` n `6`; index avg `-0.0609` n `26`; metal avg `-0.0071` n `20`; unknown avg `5.6715` n `822`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
