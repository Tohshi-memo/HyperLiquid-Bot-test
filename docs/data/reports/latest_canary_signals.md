# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T16:37:25.110699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.26` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.368` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2249` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.055` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6407` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1139` n `12`; crypto_alt avg `0.2195` n `228`; crypto_major avg `0.0815` n `8`; equity avg `-0.2105` n `69`; fx avg `0.0028` n `6`; index avg `0.0116` n `23`; metal avg `-0.1341` n `18`; unknown avg `-0.0772` n `422`
- 1h: commodity avg `0.4529` n `12`; crypto_alt avg `2.1634` n `228`; crypto_major avg `1.205` n `8`; equity avg `0.1184` n `69`; fx avg `0.009` n `6`; index avg `-0.0258` n `23`; metal avg `-0.4357` n `18`; unknown avg `1.8108` n `422`
- 4h: commodity avg `0.587` n `12`; crypto_alt avg `-1.6819` n `228`; crypto_major avg `-1.781` n `8`; equity avg `0.274` n `69`; fx avg `0.0016` n `6`; index avg `0.4439` n `23`; metal avg `-0.6764` n `18`; unknown avg `0.2047` n `422`
- 24h: commodity avg `-0.9617` n `12`; crypto_alt avg `-1.7642` n `228`; crypto_major avg `-2.3338` n `8`; equity avg `0.7044` n `69`; fx avg `0.1426` n `6`; index avg `0.7051` n `23`; metal avg `0.7129` n `18`; unknown avg `0.1509` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
