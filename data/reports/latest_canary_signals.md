# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T03:07:28.501997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0391` n `12`; crypto_alt avg `0.0618` n `228`; crypto_major avg `0.013` n `8`; equity avg `-0.006` n `74`; fx avg `0.0122` n `6`; index avg `0.0245` n `23`; metal avg `0.002` n `18`; unknown avg `-1.0713` n `645`
- 1h: commodity avg `0.0082` n `12`; crypto_alt avg `-0.1529` n `228`; crypto_major avg `-0.0347` n `8`; equity avg `-0.0917` n `74`; fx avg `-0.0101` n `6`; index avg `-0.0204` n `23`; metal avg `0.0254` n `18`; unknown avg `-1.177` n `629`
- 4h: commodity avg `-0.2517` n `12`; crypto_alt avg `-0.2259` n `228`; crypto_major avg `0.0836` n `8`; equity avg `-0.0458` n `74`; fx avg `-0.0116` n `6`; index avg `-0.0191` n `23`; metal avg `0.0091` n `18`; unknown avg `-0.869` n `629`
- 24h: commodity avg `-0.6697` n `12`; crypto_alt avg `1.3567` n `228`; crypto_major avg `1.4257` n `8`; equity avg `0.3695` n `74`; fx avg `-0.0079` n `6`; index avg `0.2213` n `23`; metal avg `0.2882` n `18`; unknown avg `-1.6582` n `595`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
