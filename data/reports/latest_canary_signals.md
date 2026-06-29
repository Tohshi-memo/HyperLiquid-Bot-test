# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T18:22:33.791971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.24` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.7326` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5583` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.085` n `12`; crypto_alt avg `-0.0277` n `228`; crypto_major avg `0.1397` n `8`; equity avg `0.0975` n `88`; fx avg `-0.0104` n `6`; index avg `0.0201` n `23`; metal avg `0.0269` n `20`; unknown avg `-0.0143` n `765`
- 1h: commodity avg `-0.1656` n `12`; crypto_alt avg `0.0725` n `228`; crypto_major avg `0.1986` n `8`; equity avg `0.2328` n `88`; fx avg `-0.0157` n `6`; index avg `0.0557` n `23`; metal avg `0.2839` n `20`; unknown avg `0.6088` n `765`
- 4h: commodity avg `-0.016` n `12`; crypto_alt avg `1.8692` n `228`; crypto_major avg `2.7166` n `8`; equity avg `2.53` n `88`; fx avg `-0.007` n `6`; index avg `0.3381` n `23`; metal avg `0.1583` n `20`; unknown avg `1.492` n `764`
- 24h: commodity avg `-0.5727` n `12`; crypto_alt avg `1.8837` n `228`; crypto_major avg `2.8755` n `8`; equity avg `1.4993` n `88`; fx avg `0.1198` n `6`; index avg `0.1573` n `23`; metal avg `-0.3968` n `20`; unknown avg `3.3606` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
