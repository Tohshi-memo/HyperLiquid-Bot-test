# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T05:52:26.864122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.1751` n `228`; crypto_major avg `-0.1094` n `8`; equity avg `-0.0194` n `78`; fx avg `-0.0044` n `6`; index avg `0.0011` n `23`; metal avg `-0.0005` n `18`; unknown avg `0.0674` n `702`
- 1h: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.1186` n `228`; crypto_major avg `-0.1926` n `8`; equity avg `0.0336` n `78`; fx avg `-0.0019` n `6`; index avg `0.0171` n `23`; metal avg `-0.0018` n `18`; unknown avg `3.0707` n `678`
- 4h: commodity avg `0.0335` n `12`; crypto_alt avg `-0.397` n `228`; crypto_major avg `-0.4449` n `8`; equity avg `0.1393` n `78`; fx avg `-0.0179` n `6`; index avg `0.0283` n `23`; metal avg `0.0175` n `18`; unknown avg `-0.1331` n `678`
- 24h: commodity avg `0.1664` n `12`; crypto_alt avg `0.8927` n `228`; crypto_major avg `0.3201` n `8`; equity avg `0.1898` n `78`; fx avg `0.0605` n `6`; index avg `-0.0269` n `23`; metal avg `-0.0297` n `18`; unknown avg `-0.2515` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
