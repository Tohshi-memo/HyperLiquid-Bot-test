# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T00:52:25.881754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0888` n `12`; crypto_alt avg `-0.0333` n `230`; crypto_major avg `-0.0557` n `8`; equity avg `-0.0486` n `102`; fx avg `0.0119` n `6`; index avg `0.0308` n `25`; metal avg `0.0002` n `20`; unknown avg `-0.0348` n `778`
- 1h: commodity avg `0.085` n `12`; crypto_alt avg `-0.1793` n `230`; crypto_major avg `-0.2284` n `8`; equity avg `0.2133` n `102`; fx avg `-0.041` n `6`; index avg `0.0265` n `25`; metal avg `-0.1672` n `20`; unknown avg `-0.0924` n `778`
- 4h: commodity avg `-0.0171` n `12`; crypto_alt avg `0.8511` n `230`; crypto_major avg `0.4677` n `8`; equity avg `0.8311` n `102`; fx avg `-0.0266` n `6`; index avg `0.1842` n `25`; metal avg `0.064` n `20`; unknown avg `0.6609` n `778`
- 24h: commodity avg `0.6263` n `12`; crypto_alt avg `-2.455` n `230`; crypto_major avg `-0.8623` n `8`; equity avg `-3.7137` n `102`; fx avg `-0.0201` n `6`; index avg `-0.6697` n `25`; metal avg `0.1939` n `20`; unknown avg `-0.6479` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
