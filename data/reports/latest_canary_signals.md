# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T12:07:32.870278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0545` n `13`; crypto_alt avg `-0.0423` n `235`; crypto_major avg `-0.0475` n `8`; equity avg `0.036` n `150`; fx avg `0.004` n `6`; index avg `0.0011` n `26`; metal avg `-0.0078` n `20`; unknown avg `0.0549` n `1066`
- 1h: commodity avg `-0.0698` n `13`; crypto_alt avg `0.1048` n `235`; crypto_major avg `0.1979` n `8`; equity avg `0.2652` n `150`; fx avg `0.0574` n `6`; index avg `0.0786` n `26`; metal avg `0.1663` n `20`; unknown avg `1.2565` n `1066`
- 4h: commodity avg `-0.3723` n `13`; crypto_alt avg `0.4337` n `235`; crypto_major avg `0.3849` n `8`; equity avg `0.3752` n `149`; fx avg `0.0908` n `6`; index avg `0.1053` n `26`; metal avg `0.1422` n `20`; unknown avg `0.8655` n `1066`
- 24h: commodity avg `-0.7245` n `13`; crypto_alt avg `-0.4511` n `235`; crypto_major avg `-0.0633` n `8`; equity avg `0.8822` n `149`; fx avg `0.0795` n `6`; index avg `0.2799` n `26`; metal avg `-0.0378` n `20`; unknown avg `-0.2366` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
