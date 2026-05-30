# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T05:37:19.024362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0468` n `228`; crypto_major avg `0.0633` n `8`; equity avg `0.0389` n `69`; fx avg `0.0015` n `6`; index avg `-0.0048` n `23`; metal avg `-0.0007` n `18`; unknown avg `0.1081` n `419`
- 1h: commodity avg `0.057` n `12`; crypto_alt avg `1.0834` n `228`; crypto_major avg `0.8761` n `8`; equity avg `0.2453` n `69`; fx avg `0.0001` n `6`; index avg `0.0259` n `23`; metal avg `0.0409` n `18`; unknown avg `0.9189` n `419`
- 4h: commodity avg `-0.2339` n `12`; crypto_alt avg `-0.0354` n `228`; crypto_major avg `0.1598` n `8`; equity avg `0.1892` n `69`; fx avg `-0.0048` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0201` n `18`; unknown avg `0.4261` n `419`
- 24h: commodity avg `-0.2618` n `12`; crypto_alt avg `1.8977` n `228`; crypto_major avg `2.1633` n `8`; equity avg `1.0387` n `69`; fx avg `0.0869` n `6`; index avg `0.0227` n `23`; metal avg `0.0082` n `18`; unknown avg `1.657` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
