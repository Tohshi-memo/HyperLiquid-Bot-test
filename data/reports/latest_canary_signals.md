# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T14:52:32.043476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.35` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `3.2478` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.199` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.988` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1271` n `12`; crypto_alt avg `0.1446` n `233`; crypto_major avg `0.0766` n `8`; equity avg `-0.0077` n `136`; fx avg `-0.0141` n `6`; index avg `-0.0023` n `26`; metal avg `0.0841` n `20`; unknown avg `1.2568` n `796`
- 1h: commodity avg `0.0267` n `12`; crypto_alt avg `0.4397` n `233`; crypto_major avg `0.0547` n `8`; equity avg `0.0808` n `136`; fx avg `0.0223` n `6`; index avg `0.0058` n `26`; metal avg `-0.0637` n `20`; unknown avg `7.9915` n `778`
- 4h: commodity avg `0.1652` n `12`; crypto_alt avg `3.2181` n `233`; crypto_major avg `3.413` n `8`; equity avg `0.425` n `136`; fx avg `-0.0453` n `6`; index avg `0.0718` n `26`; metal avg `0.214` n `20`; unknown avg `5.3449` n `772`
- 24h: commodity avg `-0.0646` n `12`; crypto_alt avg `1.9906` n `233`; crypto_major avg `2.9233` n `8`; equity avg `-0.0005` n `136`; fx avg `-0.1472` n `6`; index avg `0.1993` n `26`; metal avg `0.1566` n `20`; unknown avg `5.3783` n `697`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
