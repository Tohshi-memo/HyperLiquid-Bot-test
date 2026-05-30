# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T05:22:22.071280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0244` n `12`; crypto_alt avg `0.0693` n `228`; crypto_major avg `0.1547` n `8`; equity avg `0.0392` n `69`; fx avg `0.0002` n `6`; index avg `0.016` n `23`; metal avg `-0.0176` n `18`; unknown avg `-0.0272` n `419`
- 1h: commodity avg `-0.0751` n `12`; crypto_alt avg `0.4022` n `228`; crypto_major avg `0.384` n `8`; equity avg `0.1839` n `69`; fx avg `-0.0025` n `6`; index avg `0.0542` n `23`; metal avg `0.04` n `18`; unknown avg `0.2281` n `419`
- 4h: commodity avg `-0.1184` n `12`; crypto_alt avg `0.2176` n `228`; crypto_major avg `0.2979` n `8`; equity avg `0.2075` n `69`; fx avg `0.0015` n `6`; index avg `-0.023` n `23`; metal avg `-0.0079` n `18`; unknown avg `0.4501` n `419`
- 24h: commodity avg `-0.1917` n `12`; crypto_alt avg `1.8171` n `228`; crypto_major avg `1.9152` n `8`; equity avg `0.8169` n `69`; fx avg `0.0781` n `6`; index avg `0.0404` n `23`; metal avg `-0.1138` n `18`; unknown avg `1.5576` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
