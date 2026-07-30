# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T02:52:30.234933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.1137` n `230`; crypto_major avg `0.077` n `8`; equity avg `0.0781` n `102`; fx avg `0.0019` n `6`; index avg `0.001` n `25`; metal avg `-0.0238` n `20`; unknown avg `-0.0082` n `779`
- 1h: commodity avg `-0.0561` n `12`; crypto_alt avg `-0.0247` n `230`; crypto_major avg `-0.1189` n `8`; equity avg `-1.0168` n `102`; fx avg `-0.0482` n `6`; index avg `-0.2352` n `25`; metal avg `-0.1699` n `20`; unknown avg `-0.0919` n `779`
- 4h: commodity avg `-0.1588` n `12`; crypto_alt avg `0.8775` n `230`; crypto_major avg `0.5022` n `8`; equity avg `0.6508` n `102`; fx avg `-0.0367` n `6`; index avg `0.1499` n `25`; metal avg `-0.1004` n `20`; unknown avg `0.1345` n `778`
- 24h: commodity avg `0.4839` n `12`; crypto_alt avg `-0.712` n `230`; crypto_major avg `0.0842` n `8`; equity avg `-1.8913` n `102`; fx avg `0.0348` n `6`; index avg `-0.0568` n `25`; metal avg `0.1878` n `20`; unknown avg `-0.5935` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
