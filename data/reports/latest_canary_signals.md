# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T17:37:34.121656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0649` n `12`; crypto_alt avg `0.1125` n `229`; crypto_major avg `0.1776` n `8`; equity avg `0.1806` n `91`; fx avg `-0.0011` n `6`; index avg `0.0465` n `25`; metal avg `0.0321` n `20`; unknown avg `0.0169` n `764`
- 1h: commodity avg `-0.2953` n `12`; crypto_alt avg `0.8253` n `229`; crypto_major avg `0.8689` n `8`; equity avg `0.727` n `91`; fx avg `-0.0076` n `6`; index avg `0.1764` n `25`; metal avg `0.3294` n `20`; unknown avg `0.3387` n `764`
- 4h: commodity avg `-0.1425` n `12`; crypto_alt avg `0.5389` n `229`; crypto_major avg `0.4091` n `8`; equity avg `0.366` n `91`; fx avg `0.0525` n `6`; index avg `0.2129` n `25`; metal avg `-0.0938` n `20`; unknown avg `-0.0894` n `764`
- 24h: commodity avg `0.6245` n `12`; crypto_alt avg `-3.0448` n `229`; crypto_major avg `-3.4522` n `8`; equity avg `-0.1408` n `91`; fx avg `0.0141` n `6`; index avg `-0.1472` n `25`; metal avg `-1.235` n `20`; unknown avg `0.1839` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
