# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T08:52:30.511819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.058` n `13`; crypto_alt avg `-0.2219` n `239`; crypto_major avg `-0.2777` n `8`; equity avg `-0.1422` n `165`; fx avg `-0.019` n `6`; index avg `-0.013` n `27`; metal avg `-0.0686` n `20`; unknown avg `0.1161` n `1262`
- 1h: commodity avg `-0.3095` n `13`; crypto_alt avg `0.0301` n `239`; crypto_major avg `-0.1991` n `8`; equity avg `0.0722` n `165`; fx avg `-0.0456` n `6`; index avg `0.0221` n `27`; metal avg `0.0828` n `20`; unknown avg `4.0006` n `1206`
- 4h: commodity avg `-0.4949` n `13`; crypto_alt avg `0.8939` n `239`; crypto_major avg `0.8273` n `8`; equity avg `0.0752` n `165`; fx avg `-0.055` n `6`; index avg `0.0594` n `27`; metal avg `0.5148` n `20`; unknown avg `42.7553` n `1188`
- 24h: commodity avg `-0.4766` n `13`; crypto_alt avg `-3.1607` n `239`; crypto_major avg `-2.6267` n `8`; equity avg `-6.8118` n `165`; fx avg `-0.0856` n `6`; index avg `-0.6155` n `27`; metal avg `-1.3396` n `20`; unknown avg `18.8038` n `1161`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
