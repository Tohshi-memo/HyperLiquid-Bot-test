# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T22:22:20.247805+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `12`; crypto_alt avg `0.4594` n `228`; crypto_major avg `0.3143` n `8`; equity avg `0.0715` n `69`; fx avg `0.002` n `6`; index avg `-0.0138` n `23`; metal avg `0.0474` n `18`; unknown avg `0.0878` n `419`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `-0.2079` n `228`; crypto_major avg `-0.0945` n `8`; equity avg `0.0123` n `69`; fx avg `-0.0038` n `6`; index avg `0.0288` n `23`; metal avg `0.0548` n `18`; unknown avg `0.943` n `419`
- 4h: commodity avg `0.2143` n `12`; crypto_alt avg `-0.6633` n `228`; crypto_major avg `-0.4346` n `8`; equity avg `0.1261` n `69`; fx avg `-0.0149` n `6`; index avg `0.0123` n `23`; metal avg `-0.1782` n `18`; unknown avg `0.5978` n `419`
- 24h: commodity avg `-0.5862` n `12`; crypto_alt avg `0.6057` n `228`; crypto_major avg `0.8427` n `8`; equity avg `0.9159` n `69`; fx avg `0.1867` n `6`; index avg `0.0733` n `23`; metal avg `0.0851` n `18`; unknown avg `1.1699` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
