# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T18:52:31.768851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.63` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.0543` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9435` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.0331` n `228`; crypto_major avg `-0.051` n `8`; equity avg `0.0992` n `88`; fx avg `0.0007` n `6`; index avg `0.0153` n `23`; metal avg `-0.0101` n `20`; unknown avg `0.0115` n `765`
- 1h: commodity avg `-0.1356` n `12`; crypto_alt avg `-0.2518` n `228`; crypto_major avg `-0.3974` n `8`; equity avg `0.1826` n `88`; fx avg `-0.0078` n `6`; index avg `0.0385` n `23`; metal avg `0.0518` n `20`; unknown avg `0.1599` n `765`
- 4h: commodity avg `-0.0429` n `12`; crypto_alt avg `1.3966` n `228`; crypto_major avg `2.0114` n `8`; equity avg `1.878` n `88`; fx avg `-0.0105` n `6`; index avg `0.2645` n `23`; metal avg `0.0679` n `20`; unknown avg `1.235` n `764`
- 24h: commodity avg `-0.58` n `12`; crypto_alt avg `1.733` n `228`; crypto_major avg `2.4989` n `8`; equity avg `1.6159` n `88`; fx avg `0.1288` n `6`; index avg `0.1941` n `23`; metal avg `-0.4457` n `20`; unknown avg `1.3396` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
