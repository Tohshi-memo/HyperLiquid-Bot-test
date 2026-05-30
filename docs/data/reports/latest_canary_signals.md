# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T02:37:16.239490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `0.179` n `228`; crypto_major avg `-0.035` n `8`; equity avg `0.0538` n `69`; fx avg `0.0006` n `6`; index avg `0.0105` n `23`; metal avg `0.0104` n `18`; unknown avg `-0.1654` n `419`
- 1h: commodity avg `-0.2062` n `12`; crypto_alt avg `0.3396` n `228`; crypto_major avg `0.1874` n `8`; equity avg `0.0474` n `69`; fx avg `-0.0057` n `6`; index avg `-0.0402` n `23`; metal avg `0.0132` n `18`; unknown avg `-0.2659` n `419`
- 4h: commodity avg `0.0008` n `12`; crypto_alt avg `1.7737` n `228`; crypto_major avg `1.2064` n `8`; equity avg `0.2741` n `69`; fx avg `-0.0096` n `6`; index avg `-0.0445` n `23`; metal avg `0.0443` n `18`; unknown avg `-0.2571` n `419`
- 24h: commodity avg `-0.2626` n `12`; crypto_alt avg `2.1856` n `228`; crypto_major avg `2.3291` n `8`; equity avg `1.2901` n `69`; fx avg `0.108` n `6`; index avg `0.1834` n `23`; metal avg `0.0281` n `18`; unknown avg `0.6154` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
