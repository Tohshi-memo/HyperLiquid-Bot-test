# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T03:37:32.237258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1911` n `12`; crypto_alt avg `-0.0198` n `228`; crypto_major avg `0.0582` n `8`; equity avg `-0.012` n `74`; fx avg `0.0086` n `6`; index avg `0.1401` n `23`; metal avg `-0.0717` n `18`; unknown avg `-0.6078` n `637`
- 1h: commodity avg `0.1594` n `12`; crypto_alt avg `0.1259` n `228`; crypto_major avg `-0.0109` n `8`; equity avg `0.1724` n `74`; fx avg `0.0005` n `6`; index avg `0.021` n `23`; metal avg `-0.3066` n `18`; unknown avg `-0.3773` n `637`
- 4h: commodity avg `-0.3066` n `12`; crypto_alt avg `0.6603` n `228`; crypto_major avg `0.3423` n `8`; equity avg `0.6939` n `74`; fx avg `-0.0854` n `6`; index avg `0.5284` n `23`; metal avg `0.5761` n `18`; unknown avg `-0.5768` n `629`
- 24h: commodity avg `-0.9434` n `12`; crypto_alt avg `2.3158` n `228`; crypto_major avg `2.5001` n `8`; equity avg `1.8384` n `74`; fx avg `0.0134` n `6`; index avg `0.9485` n `23`; metal avg `2.0038` n `18`; unknown avg `3.2661` n `585`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
