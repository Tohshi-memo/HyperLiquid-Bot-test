# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T08:22:21.679977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1298` n `12`; crypto_alt avg `0.2663` n `228`; crypto_major avg `0.1377` n `8`; equity avg `-0.0482` n `69`; fx avg `-0.0091` n `6`; index avg `0.0129` n `23`; metal avg `-0.087` n `18`; unknown avg `-0.0407` n `417`
- 1h: commodity avg `0.2793` n `12`; crypto_alt avg `-0.1501` n `228`; crypto_major avg `0.1005` n `8`; equity avg `-0.0975` n `69`; fx avg `-0.0321` n `6`; index avg `0.012` n `23`; metal avg `-0.1453` n `18`; unknown avg `0.9432` n `417`
- 4h: commodity avg `0.5259` n `12`; crypto_alt avg `1.0614` n `228`; crypto_major avg `1.0547` n `8`; equity avg `0.202` n `69`; fx avg `0.0405` n `6`; index avg `0.0509` n `23`; metal avg `-0.1364` n `18`; unknown avg `1.2784` n `407`
- 24h: commodity avg `0.6747` n `12`; crypto_alt avg `1.6689` n `228`; crypto_major avg `2.348` n `8`; equity avg `3.4151` n `69`; fx avg `0.1441` n `6`; index avg `1.2008` n `23`; metal avg `1.4985` n `18`; unknown avg `1.8336` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
