# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T17:37:27.049326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.84` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6584` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0453` n `229`; crypto_major avg `0.1656` n `8`; equity avg `0.0851` n `91`; fx avg `0.0013` n `6`; index avg `0.0091` n `25`; metal avg `0.0583` n `20`; unknown avg `0.1513` n `763`
- 1h: commodity avg `0.0819` n `12`; crypto_alt avg `-0.1451` n `229`; crypto_major avg `0.2043` n `8`; equity avg `0.2221` n `91`; fx avg `0.0106` n `6`; index avg `0.0445` n `25`; metal avg `0.018` n `20`; unknown avg `0.5524` n `763`
- 4h: commodity avg `0.3692` n `12`; crypto_alt avg `0.4206` n `229`; crypto_major avg `1.2427` n `8`; equity avg `-0.4157` n `91`; fx avg `-0.0476` n `6`; index avg `-0.0076` n `25`; metal avg `-0.2273` n `20`; unknown avg `1.6456` n `755`
- 24h: commodity avg `0.6682` n `12`; crypto_alt avg `-0.7727` n `229`; crypto_major avg `0.0591` n `8`; equity avg `-2.6448` n `91`; fx avg `-0.2465` n `6`; index avg `-0.4581` n `25`; metal avg `-0.1206` n `20`; unknown avg `1.0771` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0506`, n `668`, weak_sample_signal
