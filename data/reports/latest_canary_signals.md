# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T16:07:33.702986+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.34` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `2.7415` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.5549` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.4769` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.969` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1286` n `12`; crypto_alt avg `0.7419` n `228`; crypto_major avg `0.5125` n `8`; equity avg `0.121` n `69`; fx avg `0.0071` n `6`; index avg `0.0179` n `23`; metal avg `-0.0734` n `18`; unknown avg `0.9556` n `422`
- 1h: commodity avg `0.2368` n `12`; crypto_alt avg `-0.7716` n `228`; crypto_major avg `-0.4158` n `8`; equity avg `0.4008` n `69`; fx avg `0.0193` n `6`; index avg `0.1705` n `23`; metal avg `0.0295` n `18`; unknown avg `-0.0683` n `422`
- 4h: commodity avg `0.2643` n `12`; crypto_alt avg `-2.5104` n `228`; crypto_major avg `-2.2126` n `8`; equity avg `0.3423` n `69`; fx avg `0.008` n `6`; index avg `0.5289` n `23`; metal avg `-0.2436` n `18`; unknown avg `0.2151` n `422`
- 24h: commodity avg `-0.9886` n `12`; crypto_alt avg `-2.006` n `228`; crypto_major avg `-2.2763` n `8`; equity avg `0.6852` n `69`; fx avg `0.1822` n `6`; index avg `0.8117` n `23`; metal avg `0.9268` n `18`; unknown avg `-0.1321` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
