# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T00:52:23.693016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `0.1728` n `228`; crypto_major avg `0.1337` n `8`; equity avg `0.111` n `69`; fx avg `0.0012` n `6`; index avg `0.0362` n `23`; metal avg `0.0141` n `18`; unknown avg `0.082` n `419`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `0.5456` n `228`; crypto_major avg `0.3681` n `8`; equity avg `0.115` n `69`; fx avg `0.0027` n `6`; index avg `-0.0004` n `23`; metal avg `0.0052` n `18`; unknown avg `-0.1106` n `419`
- 4h: commodity avg `0.2971` n `12`; crypto_alt avg `0.3847` n `228`; crypto_major avg `0.1212` n `8`; equity avg `0.1099` n `69`; fx avg `-0.0209` n `6`; index avg `0.0467` n `23`; metal avg `0.0631` n `18`; unknown avg `0.4286` n `419`
- 24h: commodity avg `-0.1608` n `12`; crypto_alt avg `0.5809` n `228`; crypto_major avg `0.8654` n `8`; equity avg `0.9062` n `69`; fx avg `0.0973` n `6`; index avg `0.2059` n `23`; metal avg `0.0964` n `18`; unknown avg `1.1644` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
