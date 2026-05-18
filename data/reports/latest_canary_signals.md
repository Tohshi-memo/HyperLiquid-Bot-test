# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T20:37:19.953769+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1007` n `12`; crypto_alt avg `0.0584` n `228`; crypto_major avg `-0.1225` n `8`; equity avg `0.0469` n `66`; fx avg `-0.0032` n `6`; index avg `-0.0313` n `23`; metal avg `-0.0516` n `18`; unknown avg `-0.1477` n `383`
- 1h: commodity avg `-0.1263` n `12`; crypto_alt avg `0.4838` n `228`; crypto_major avg `0.464` n `8`; equity avg `0.4155` n `66`; fx avg `0.0262` n `6`; index avg `0.1882` n `23`; metal avg `0.1902` n `18`; unknown avg `0.1794` n `383`
- 4h: commodity avg `-0.3971` n `12`; crypto_alt avg `1.077` n `228`; crypto_major avg `0.9904` n `8`; equity avg `0.5398` n `66`; fx avg `-0.0273` n `6`; index avg `0.1544` n `23`; metal avg `0.4155` n `18`; unknown avg `0.2949` n `383`
- 24h: commodity avg `0.6951` n `12`; crypto_alt avg `-1.6721` n `228`; crypto_major avg `-1.9828` n `8`; equity avg `-0.9171` n `66`; fx avg `0.1839` n `6`; index avg `-0.4364` n `23`; metal avg `0.9992` n `18`; unknown avg `-0.0929` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
