# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T20:07:25.658007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `0.0953` n `228`; crypto_major avg `0.0008` n `8`; equity avg `0.1644` n `69`; fx avg `0.0152` n `6`; index avg `0.0477` n `23`; metal avg `-0.0152` n `18`; unknown avg `-0.1744` n `419`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `0.0427` n `228`; crypto_major avg `0.2441` n `8`; equity avg `0.5708` n `69`; fx avg `0.0281` n `6`; index avg `0.1313` n `23`; metal avg `-0.1286` n `18`; unknown avg `-0.2974` n `419`
- 4h: commodity avg `-0.2521` n `12`; crypto_alt avg `-0.6255` n `228`; crypto_major avg `-0.2538` n `8`; equity avg `0.0899` n `69`; fx avg `0.0168` n `6`; index avg `0.095` n `23`; metal avg `-0.1529` n `18`; unknown avg `-0.2919` n `419`
- 24h: commodity avg `-0.7958` n `12`; crypto_alt avg `1.2085` n `228`; crypto_major avg `1.5311` n `8`; equity avg `1.5428` n `69`; fx avg `0.2389` n `6`; index avg `0.1107` n `23`; metal avg `0.1783` n `18`; unknown avg `1.6217` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
