# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T09:52:26.281477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0389` n `12`; crypto_alt avg `0.0257` n `230`; crypto_major avg `0.0222` n `8`; equity avg `-0.101` n `102`; fx avg `-0.0284` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0408` n `20`; unknown avg `-0.0129` n `774`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `0.0391` n `230`; crypto_major avg `0.0874` n `8`; equity avg `-0.2977` n `102`; fx avg `-0.0394` n `6`; index avg `-0.0656` n `25`; metal avg `-0.1675` n `20`; unknown avg `-0.0318` n `774`
- 4h: commodity avg `-0.3416` n `12`; crypto_alt avg `-0.1013` n `230`; crypto_major avg `-0.0802` n `8`; equity avg `-0.0256` n `102`; fx avg `-0.0338` n `6`; index avg `0.0103` n `25`; metal avg `-0.0917` n `20`; unknown avg `0.0357` n `758`
- 24h: commodity avg `-0.4148` n `12`; crypto_alt avg `-3.5426` n `230`; crypto_major avg `-3.5464` n `8`; equity avg `-4.342` n `102`; fx avg `-0.1775` n `6`; index avg `-0.9047` n `25`; metal avg `-0.6265` n `20`; unknown avg `998.0751` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
