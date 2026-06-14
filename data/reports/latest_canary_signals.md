# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T04:22:30.670605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0112` n `228`; crypto_major avg `-0.0448` n `8`; equity avg `-0.0143` n `74`; fx avg `-0.0097` n `6`; index avg `0.0026` n `23`; metal avg `0.006` n `18`; unknown avg `2.3156` n `645`
- 1h: commodity avg `-0.0594` n `12`; crypto_alt avg `-0.0044` n `228`; crypto_major avg `-0.0396` n `8`; equity avg `0.0172` n `74`; fx avg `-0.0131` n `6`; index avg `0.0177` n `23`; metal avg `-0.0007` n `18`; unknown avg `2.1053` n `645`
- 4h: commodity avg `-0.0624` n `12`; crypto_alt avg `-0.0225` n `228`; crypto_major avg `0.1026` n `8`; equity avg `0.1587` n `74`; fx avg `-0.0021` n `6`; index avg `0.0024` n `23`; metal avg `0.0213` n `18`; unknown avg `-1.5795` n `629`
- 24h: commodity avg `-0.6881` n `12`; crypto_alt avg `1.7475` n `228`; crypto_major avg `1.7705` n `8`; equity avg `0.6842` n `74`; fx avg `-0.0116` n `6`; index avg `0.2458` n `23`; metal avg `0.3313` n `18`; unknown avg `-1.7551` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
