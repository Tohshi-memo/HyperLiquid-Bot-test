# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T14:37:29.598588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.33` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `3.1846` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.0364` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.9056` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `2.3276` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.831` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.3531` n `233`; crypto_major avg `-0.2601` n `8`; equity avg `-0.2631` n `136`; fx avg `0.0154` n `6`; index avg `-0.0515` n `26`; metal avg `-0.1144` n `20`; unknown avg `0.2548` n `796`
- 1h: commodity avg `0.2421` n `12`; crypto_alt avg `1.9372` n `233`; crypto_major avg `2.1676` n `8`; equity avg `0.3366` n `136`; fx avg `0.0622` n `6`; index avg `-0.0218` n `26`; metal avg `-0.16` n `20`; unknown avg `8.4245` n `778`
- 4h: commodity avg `0.2474` n `12`; crypto_alt avg `2.9496` n `233`; crypto_major avg `3.2838` n `8`; equity avg `0.3782` n `136`; fx avg `-0.0337` n `6`; index avg `0.0696` n `26`; metal avg `0.0992` n `20`; unknown avg `5.2627` n `772`
- 24h: commodity avg `0.1831` n `12`; crypto_alt avg `1.6019` n `233`; crypto_major avg `2.6913` n `8`; equity avg `-0.1455` n `136`; fx avg `-0.1163` n `6`; index avg `0.1501` n `26`; metal avg `-0.0272` n `20`; unknown avg `5.1904` n `683`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
