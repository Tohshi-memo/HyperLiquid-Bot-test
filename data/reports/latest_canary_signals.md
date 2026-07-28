# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T18:06:09.292891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `0.2599` n `230`; crypto_major avg `0.2697` n `8`; equity avg `0.0062` n `102`; fx avg `-0.0051` n `6`; index avg `0.0028` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0342` n `774`
- 1h: commodity avg `0.1548` n `12`; crypto_alt avg `-0.3777` n `230`; crypto_major avg `-0.5126` n `8`; equity avg `-0.5504` n `102`; fx avg `-0.0346` n `6`; index avg `-0.0955` n `25`; metal avg `-0.1105` n `20`; unknown avg `0.0066` n `774`
- 4h: commodity avg `-0.5278` n `12`; crypto_alt avg `0.5059` n `230`; crypto_major avg `0.9354` n `8`; equity avg `1.103` n `102`; fx avg `-0.0572` n `6`; index avg `0.1479` n `25`; metal avg `0.0418` n `20`; unknown avg `-0.0586` n `774`
- 24h: commodity avg `-0.8969` n `12`; crypto_alt avg `-2.0701` n `230`; crypto_major avg `-1.973` n `8`; equity avg `-2.9987` n `102`; fx avg `-0.1085` n `6`; index avg `-0.2851` n `25`; metal avg `-0.415` n `20`; unknown avg `-0.5051` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
