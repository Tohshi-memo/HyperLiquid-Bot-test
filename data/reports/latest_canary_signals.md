# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T16:22:29.690821+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0883` n `12`; crypto_alt avg `-0.0898` n `228`; crypto_major avg `-0.1117` n `8`; equity avg `0.0372` n `74`; fx avg `0.0` n `6`; index avg `0.0012` n `23`; metal avg `0.0305` n `18`; unknown avg `-0.0524` n `644`
- 1h: commodity avg `-0.0686` n `12`; crypto_alt avg `-0.5319` n `228`; crypto_major avg `-0.5578` n `8`; equity avg `-0.0433` n `74`; fx avg `-0.0045` n `6`; index avg `0.0395` n `23`; metal avg `0.0101` n `18`; unknown avg `-0.0787` n `644`
- 4h: commodity avg `-0.1051` n `12`; crypto_alt avg `0.0398` n `228`; crypto_major avg `0.2428` n `8`; equity avg `0.2927` n `74`; fx avg `-0.0124` n `6`; index avg `0.2183` n `23`; metal avg `0.0838` n `18`; unknown avg `-2.045` n `644`
- 24h: commodity avg `-0.7167` n `12`; crypto_alt avg `1.77` n `228`; crypto_major avg `0.3252` n `8`; equity avg `0.3946` n `74`; fx avg `0.0242` n `6`; index avg `0.7329` n `23`; metal avg `0.3203` n `18`; unknown avg `-1.9598` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
