# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T17:52:27.109998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.02` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `2.2316` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1066` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0609` n `228`; crypto_major avg `0.1605` n `8`; equity avg `0.0709` n `88`; fx avg `-0.0005` n `6`; index avg `0.0142` n `23`; metal avg `0.2264` n `20`; unknown avg `0.0765` n `765`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `1.008` n `228`; crypto_major avg `1.6107` n `8`; equity avg `0.4737` n `88`; fx avg `-0.009` n `6`; index avg `0.0561` n `23`; metal avg `0.2015` n `20`; unknown avg `0.2265` n `765`
- 4h: commodity avg `0.1048` n `12`; crypto_alt avg `1.3968` n `228`; crypto_major avg `2.2114` n `8`; equity avg `1.0383` n `88`; fx avg `0.0045` n `6`; index avg `0.0879` n `23`; metal avg `-0.0202` n `20`; unknown avg `0.8541` n `764`
- 24h: commodity avg `-0.442` n `12`; crypto_alt avg `1.85` n `228`; crypto_major avg `2.7784` n `8`; equity avg `1.4267` n `88`; fx avg `0.1316` n `6`; index avg `0.147` n `23`; metal avg `-0.4737` n `20`; unknown avg `3.5533` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
