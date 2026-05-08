# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T11:07:18.055675+00:00`
- Correlation status: `ready`
- Asset price records: `640`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0755` n `12`; crypto_alt avg `-0.1721` n `228`; crypto_major avg `-0.0818` n `8`; equity avg `-0.0286` n `65`; fx avg `-0.0016` n `5`; index avg `0.1213` n `23`; metal avg `0.0827` n `18`; unknown avg `-0.0829` n `375`
- 1h: commodity avg `-0.1804` n `12`; crypto_alt avg `0.0216` n `228`; crypto_major avg `0.1125` n `8`; equity avg `-0.0243` n `65`; fx avg `-0.0244` n `5`; index avg `-0.0225` n `23`; metal avg `0.2436` n `18`; unknown avg `-0.0259` n `375`
- 4h: commodity avg `0.1286` n `12`; crypto_alt avg `0.928` n `228`; crypto_major avg `0.7949` n `8`; equity avg `0.5891` n `65`; fx avg `0.0259` n `5`; index avg `0.1646` n `23`; metal avg `0.1097` n `18`; unknown avg `0.4301` n `375`
- 24h: commodity avg `1.2578` n `12`; crypto_alt avg `0.9638` n `228`; crypto_major avg `-1.3095` n `8`; equity avg `-0.7047` n `65`; fx avg `0.2379` n `5`; index avg `-0.42` n `23`; metal avg `-0.2882` n `18`; unknown avg `-0.2978` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1385`, n `632`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1377`, n `632`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1056`, n `636`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `636`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `636`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `632`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `636`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0801`, n `632`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `632`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `636`, weak_sample_signal
