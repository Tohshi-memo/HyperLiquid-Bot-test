# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T19:18:09.060083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.95` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.1551` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.122` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `0.0177` n `228`; crypto_major avg `0.1109` n `8`; equity avg `0.0657` n `88`; fx avg `-0.0018` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0475` n `20`; unknown avg `-0.1008` n `765`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.3181` n `228`; crypto_major avg `-0.3217` n `8`; equity avg `0.0835` n `88`; fx avg `0.001` n `6`; index avg `-0.0014` n `23`; metal avg `-0.1608` n `20`; unknown avg `0.0631` n `765`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `1.4435` n `228`; crypto_major avg `2.1805` n `8`; equity avg `1.7976` n `88`; fx avg `-0.0215` n `6`; index avg `0.2116` n `23`; metal avg `0.0585` n `20`; unknown avg `2.0515` n `765`
- 24h: commodity avg `-0.586` n `12`; crypto_alt avg `1.6903` n `228`; crypto_major avg `2.7948` n `8`; equity avg `1.6445` n `88`; fx avg `0.1544` n `6`; index avg `0.1804` n `23`; metal avg `-0.5619` n `20`; unknown avg `3.2801` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
