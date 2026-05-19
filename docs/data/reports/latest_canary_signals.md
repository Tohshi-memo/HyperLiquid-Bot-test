# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T22:22:25.537407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.1523` n `228`; crypto_major avg `-0.0455` n `8`; equity avg `-0.0811` n `66`; fx avg `-0.0047` n `6`; index avg `-0.0138` n `23`; metal avg `-0.0923` n `18`; unknown avg `0.025` n `383`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `-0.6023` n `228`; crypto_major avg `-0.4085` n `8`; equity avg `0.0466` n `66`; fx avg `-0.0005` n `6`; index avg `-0.0141` n `23`; metal avg `-0.0133` n `18`; unknown avg `0.0101` n `383`
- 4h: commodity avg `0.1802` n `12`; crypto_alt avg `-0.5489` n `228`; crypto_major avg `-0.3795` n `8`; equity avg `-0.5721` n `66`; fx avg `-0.0059` n `6`; index avg `-0.5681` n `23`; metal avg `-0.2374` n `18`; unknown avg `0.0032` n `383`
- 24h: commodity avg `1.1538` n `12`; crypto_alt avg `-1.4312` n `228`; crypto_major avg `-1.0956` n `8`; equity avg `-0.248` n `66`; fx avg `0.0543` n `6`; index avg `-0.7903` n `23`; metal avg `-2.8949` n `18`; unknown avg `0.7891` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
