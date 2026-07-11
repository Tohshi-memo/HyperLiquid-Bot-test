# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T13:37:28.878433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0113` n `12`; crypto_alt avg `0.0716` n `230`; crypto_major avg `0.0329` n `8`; equity avg `0.0344` n `92`; fx avg `0.0002` n `6`; index avg `0.0021` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0035` n `765`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `0.2426` n `230`; crypto_major avg `0.1518` n `8`; equity avg `-0.0587` n `92`; fx avg `-0.0031` n `6`; index avg `0.0011` n `25`; metal avg `0.0082` n `20`; unknown avg `0.0112` n `765`
- 4h: commodity avg `0.0227` n `12`; crypto_alt avg `0.2859` n `230`; crypto_major avg `0.202` n `8`; equity avg `-0.0857` n `92`; fx avg `-0.0071` n `6`; index avg `-0.0065` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.2181` n `765`
- 24h: commodity avg `-0.0317` n `12`; crypto_alt avg `0.4284` n `229`; crypto_major avg `-0.267` n `8`; equity avg `-0.0296` n `92`; fx avg `-0.0626` n `6`; index avg `0.1398` n `25`; metal avg `0.1609` n `20`; unknown avg `2.9142` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
