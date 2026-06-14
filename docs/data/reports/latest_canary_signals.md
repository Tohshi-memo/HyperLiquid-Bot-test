# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T03:22:29.281040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0311` n `12`; crypto_alt avg `0.0394` n `228`; crypto_major avg `-0.0042` n `8`; equity avg `0.0094` n `74`; fx avg `0.0077` n `6`; index avg `-0.0134` n `23`; metal avg `-0.0058` n `18`; unknown avg `-0.4672` n `645`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.1844` n `228`; crypto_major avg `-0.1469` n `8`; equity avg `0.0287` n `74`; fx avg `-0.0115` n `6`; index avg `-0.0363` n `23`; metal avg `0.0026` n `18`; unknown avg `-1.5068` n `629`
- 4h: commodity avg `-0.2456` n `12`; crypto_alt avg `-0.2455` n `228`; crypto_major avg `-0.0423` n `8`; equity avg `0.0842` n `74`; fx avg `0.017` n `6`; index avg `-0.0294` n `23`; metal avg `0.0084` n `18`; unknown avg `-1.5467` n `629`
- 24h: commodity avg `-0.4818` n `12`; crypto_alt avg `1.8152` n `228`; crypto_major avg `1.7672` n `8`; equity avg `0.5122` n `74`; fx avg `0.002` n `6`; index avg `0.2254` n `23`; metal avg `0.2803` n `18`; unknown avg `-1.8101` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
