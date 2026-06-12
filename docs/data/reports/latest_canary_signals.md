# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T18:07:33.933772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0128` n `12`; crypto_alt avg `-0.4989` n `228`; crypto_major avg `-0.4298` n `8`; equity avg `-0.2654` n `74`; fx avg `0.0054` n `6`; index avg `-0.133` n `23`; metal avg `-0.074` n `18`; unknown avg `0.1145` n `643`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.6856` n `228`; crypto_major avg `-0.4885` n `8`; equity avg `-0.2018` n `74`; fx avg `0.0162` n `6`; index avg `-0.0919` n `23`; metal avg `0.1299` n `18`; unknown avg `-0.0513` n `643`
- 4h: commodity avg `-0.7091` n `12`; crypto_alt avg `-0.4217` n `228`; crypto_major avg `0.2116` n `8`; equity avg `0.022` n `74`; fx avg `0.0097` n `6`; index avg `0.1987` n `23`; metal avg `0.6712` n `18`; unknown avg `2.8868` n `643`
- 24h: commodity avg `-1.0246` n `12`; crypto_alt avg `-0.1463` n `228`; crypto_major avg `1.0124` n `8`; equity avg `1.2585` n `74`; fx avg `0.0538` n `6`; index avg `1.1654` n `23`; metal avg `1.7912` n `18`; unknown avg `42.6202` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
