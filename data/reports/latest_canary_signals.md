# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T07:52:33.528629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2027` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0812` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.2586` n `239`; crypto_major avg `-0.4368` n `8`; equity avg `-0.0856` n `166`; fx avg `0.0051` n `6`; index avg `-0.0054` n `27`; metal avg `-0.0212` n `20`; unknown avg `158.4422` n `1262`
- 1h: commodity avg `-0.0332` n `13`; crypto_alt avg `-0.904` n `239`; crypto_major avg `-0.667` n `8`; equity avg `-0.1844` n `166`; fx avg `0.0023` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0699` n `20`; unknown avg `1.5221` n `1256`
- 4h: commodity avg `-0.0115` n `13`; crypto_alt avg `1.2451` n `239`; crypto_major avg `2.1912` n `8`; equity avg `0.692` n `166`; fx avg `-0.0955` n `6`; index avg `0.1038` n `27`; metal avg `0.11` n `20`; unknown avg `371.9788` n `1216`
- 24h: commodity avg `0.4209` n `13`; crypto_alt avg `-5.9701` n `239`; crypto_major avg `-6.922` n `8`; equity avg `-5.0915` n `166`; fx avg `-0.1444` n `6`; index avg `-0.5583` n `27`; metal avg `-0.4238` n `20`; unknown avg `17.0127` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
