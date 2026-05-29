# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T18:42:29.451135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9909` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5776` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0424` n `12`; crypto_alt avg `-0.0845` n `228`; crypto_major avg `0.0355` n `8`; equity avg `-0.0322` n `69`; fx avg `0.0106` n `6`; index avg `-0.0212` n `23`; metal avg `0.0558` n `18`; unknown avg `-0.0077` n `419`
- 1h: commodity avg `0.0051` n `12`; crypto_alt avg `-0.7034` n `228`; crypto_major avg `-0.5829` n `8`; equity avg `-0.2563` n `69`; fx avg `0.0073` n `6`; index avg `-0.0767` n `23`; metal avg `0.1237` n `18`; unknown avg `-0.0567` n `419`
- 4h: commodity avg `-0.9034` n `12`; crypto_alt avg `2.3895` n `228`; crypto_major avg `2.0875` n `8`; equity avg `1.0819` n `69`; fx avg `0.1021` n `6`; index avg `0.2594` n `23`; metal avg `0.5099` n `18`; unknown avg `1.7104` n `418`
- 24h: commodity avg `-1.0529` n `12`; crypto_alt avg `0.8554` n `228`; crypto_major avg `1.2728` n `8`; equity avg `1.3485` n `69`; fx avg `0.2012` n `6`; index avg `-0.0368` n `23`; metal avg `0.2586` n `18`; unknown avg `1.0684` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1887`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
