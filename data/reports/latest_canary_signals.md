# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T21:37:31.114305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2508` n `12`; crypto_alt avg `-0.0161` n `228`; crypto_major avg `-0.087` n `8`; equity avg `0.0532` n `78`; fx avg `0.01` n `6`; index avg `-0.0055` n `23`; metal avg `0.002` n `18`; unknown avg `7.2818` n `702`
- 1h: commodity avg `0.1387` n `12`; crypto_alt avg `-0.9565` n `228`; crypto_major avg `-0.7933` n `8`; equity avg `-0.0719` n `78`; fx avg `-0.0316` n `6`; index avg `-0.0107` n `23`; metal avg `-0.0342` n `18`; unknown avg `-0.0575` n `702`
- 4h: commodity avg `0.2319` n `12`; crypto_alt avg `-1.2092` n `228`; crypto_major avg `-0.7454` n `8`; equity avg `-0.127` n `78`; fx avg `-0.0856` n `6`; index avg `-0.0156` n `23`; metal avg `-0.1229` n `18`; unknown avg `0.8544` n `694`
- 24h: commodity avg `0.3616` n `12`; crypto_alt avg `0.0786` n `228`; crypto_major avg `-0.892` n `8`; equity avg `0.1312` n `78`; fx avg `-0.1421` n `6`; index avg `0.008` n `23`; metal avg `-0.1438` n `18`; unknown avg `0.7219` n `645`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
