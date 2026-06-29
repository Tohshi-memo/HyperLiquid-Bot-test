# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T19:22:43.109840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.92` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.4521` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3475` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `0.1459` n `228`; crypto_major avg `0.385` n `8`; equity avg `0.1636` n `88`; fx avg `-0.002` n `6`; index avg `0.0086` n `23`; metal avg `0.0074` n `20`; unknown avg `-0.2247` n `765`
- 1h: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.1907` n `228`; crypto_major avg `-0.0495` n `8`; equity avg `0.1811` n `88`; fx avg `0.0008` n `6`; index avg `0.0164` n `23`; metal avg `-0.1061` n `20`; unknown avg `-0.1035` n `765`
- 4h: commodity avg `0.009` n `12`; crypto_alt avg `1.5747` n `228`; crypto_major avg `2.4611` n `8`; equity avg `1.8991` n `88`; fx avg `-0.0216` n `6`; index avg `0.2296` n `23`; metal avg `0.1136` n `20`; unknown avg `2.025` n `765`
- 24h: commodity avg `-0.6021` n `12`; crypto_alt avg `1.8218` n `228`; crypto_major avg `3.0787` n `8`; equity avg `1.7485` n `88`; fx avg `0.1542` n `6`; index avg `0.1982` n `23`; metal avg `-0.5077` n `20`; unknown avg `3.1751` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
