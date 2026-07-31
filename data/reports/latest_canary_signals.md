# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T09:22:24.535550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0733` n `12`; crypto_alt avg `-0.2686` n `230`; crypto_major avg `-0.2964` n `8`; equity avg `-0.1063` n `102`; fx avg `0.0821` n `6`; index avg `0.0225` n `25`; metal avg `-0.0518` n `20`; unknown avg `-0.0539` n `780`
- 1h: commodity avg `0.2383` n `12`; crypto_alt avg `-0.4865` n `230`; crypto_major avg `-0.3588` n `8`; equity avg `0.2504` n `102`; fx avg `0.0194` n `6`; index avg `0.0562` n `25`; metal avg `-0.1241` n `20`; unknown avg `-0.0456` n `780`
- 4h: commodity avg `0.2997` n `12`; crypto_alt avg `-0.4432` n `230`; crypto_major avg `-0.8224` n `8`; equity avg `-0.0581` n `102`; fx avg `-0.0914` n `6`; index avg `-0.0279` n `25`; metal avg `-0.2185` n `20`; unknown avg `-0.106` n `747`
- 24h: commodity avg `-0.0347` n `12`; crypto_alt avg `-0.5789` n `230`; crypto_major avg `-0.3006` n `8`; equity avg `8.4562` n `102`; fx avg `-0.2391` n `6`; index avg `1.2563` n `25`; metal avg `0.1307` n `20`; unknown avg `-0.0197` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
