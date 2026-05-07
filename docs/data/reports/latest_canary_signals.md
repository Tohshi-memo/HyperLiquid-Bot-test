# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T12:52:15.676997+00:00`
- Correlation status: `ready`
- Asset price records: `551`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2173` n `12`; crypto_alt avg `-0.0232` n `228`; crypto_major avg `0.0087` n `8`; equity avg `-0.0141` n `65`; fx avg `-0.0027` n `5`; index avg `-0.0603` n `23`; metal avg `0.2057` n `18`; unknown avg `0.2212` n `365`
- 1h: commodity avg `-0.7002` n `12`; crypto_alt avg `0.6741` n `228`; crypto_major avg `0.3114` n `8`; equity avg `0.0839` n `65`; fx avg `-0.0232` n `5`; index avg `-0.0336` n `23`; metal avg `0.3437` n `18`; unknown avg `0.2865` n `365`
- 4h: commodity avg `-1.1598` n `12`; crypto_alt avg `0.4525` n `228`; crypto_major avg `-0.1284` n `8`; equity avg `0.099` n `65`; fx avg `-0.006` n `5`; index avg `-0.1838` n `23`; metal avg `0.6514` n `18`; unknown avg `0.1904` n `357`
- 24h: commodity avg `-1.7629` n `7`; crypto_alt avg `0.4855` n `223`; crypto_major avg `-2.2593` n `7`; equity avg `0.8289` n `47`; fx avg `0.0606` n `4`; index avg `0.5703` n `6`; metal avg `1.8868` n `7`; unknown avg `1.0231` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1335`, n `547`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1253`, n `547`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1107`, n `547`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `543`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `543`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `543`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0744`, n `547`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0737`, n `543`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `543`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0654`, n `543`, weak_sample_signal
