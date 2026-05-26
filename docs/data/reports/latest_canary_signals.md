# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T09:52:19.005357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.1354` n `228`; crypto_major avg `-0.0196` n `8`; equity avg `-0.0441` n `67`; fx avg `-0.0008` n `6`; index avg `0.0056` n `23`; metal avg `-0.0924` n `18`; unknown avg `-0.1529` n `417`
- 1h: commodity avg `-0.1944` n `12`; crypto_alt avg `-0.0844` n `228`; crypto_major avg `-0.0755` n `8`; equity avg `0.0601` n `67`; fx avg `0.0205` n `6`; index avg `0.1002` n `23`; metal avg `-0.2097` n `18`; unknown avg `-0.3064` n `417`
- 4h: commodity avg `0.5908` n `12`; crypto_alt avg `-0.2499` n `228`; crypto_major avg `-0.4342` n `8`; equity avg `0.1534` n `67`; fx avg `0.0305` n `6`; index avg `0.1315` n `23`; metal avg `-0.2819` n `18`; unknown avg `-0.303` n `397`
- 24h: commodity avg `1.0297` n `12`; crypto_alt avg `-0.8888` n `228`; crypto_major avg `-1.7596` n `8`; equity avg `-0.622` n `67`; fx avg `-0.0719` n `6`; index avg `-0.0029` n `23`; metal avg `-0.9676` n `18`; unknown avg `-0.4527` n `387`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
