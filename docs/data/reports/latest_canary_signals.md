# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T10:22:23.916223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `0.3587` n `230`; crypto_major avg `0.3622` n `8`; equity avg `-0.0098` n `121`; fx avg `-0.0018` n `6`; index avg `0.0076` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0648` n `794`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `0.5936` n `230`; crypto_major avg `0.6229` n `8`; equity avg `0.0736` n `121`; fx avg `-0.0008` n `6`; index avg `0.0232` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0976` n `794`
- 4h: commodity avg `-0.0122` n `12`; crypto_alt avg `2.5494` n `230`; crypto_major avg `1.4282` n `8`; equity avg `0.2552` n `121`; fx avg `-0.0408` n `6`; index avg `0.0388` n `25`; metal avg `-0.001` n `20`; unknown avg `0.3256` n `794`
- 24h: commodity avg `-0.0089` n `12`; crypto_alt avg `1.0033` n `230`; crypto_major avg `2.0113` n `8`; equity avg `0.4053` n `121`; fx avg `0.0526` n `6`; index avg `0.0482` n `25`; metal avg `0.0399` n `20`; unknown avg `2.6376` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
