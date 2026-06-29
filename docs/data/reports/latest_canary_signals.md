# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T20:37:30.130381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.0684` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7137` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `-0.0904` n `228`; crypto_major avg `-0.082` n `8`; equity avg `-0.0306` n `88`; fx avg `-0.0019` n `6`; index avg `-0.0121` n `23`; metal avg `-0.0153` n `20`; unknown avg `0.0699` n `765`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.1716` n `228`; crypto_major avg `-0.1371` n `8`; equity avg `0.0964` n `88`; fx avg `0.0072` n `6`; index avg `-0.0053` n `23`; metal avg `-0.0264` n `20`; unknown avg `-0.0249` n `765`
- 4h: commodity avg `-0.1005` n `12`; crypto_alt avg `0.8429` n `228`; crypto_major avg `1.9679` n `8`; equity avg `1.0213` n `88`; fx avg `-0.0145` n `6`; index avg `0.1244` n `23`; metal avg `0.2542` n `20`; unknown avg `1.3449` n `765`
- 24h: commodity avg `-0.348` n `12`; crypto_alt avg `1.5465` n `228`; crypto_major avg `2.8449` n `8`; equity avg `1.6364` n `88`; fx avg `0.1783` n `6`; index avg `0.154` n `23`; metal avg `-0.4946` n `20`; unknown avg `0.2192` n `732`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
