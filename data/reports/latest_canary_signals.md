# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T06:52:30.349051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0246` n `229`; crypto_major avg `0.0019` n `8`; equity avg `0.0243` n `91`; fx avg `-0.0161` n `6`; index avg `0.0069` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.9844` n `765`
- 1h: commodity avg `0.0018` n `12`; crypto_alt avg `-0.2388` n `229`; crypto_major avg `-0.3023` n `8`; equity avg `-0.1891` n `91`; fx avg `-0.068` n `6`; index avg `-0.0732` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.984` n `733`
- 4h: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.264` n `229`; crypto_major avg `-0.1551` n `8`; equity avg `-0.6001` n `91`; fx avg `-0.0782` n `6`; index avg `-0.1234` n `25`; metal avg `-0.064` n `20`; unknown avg `1.0128` n `733`
- 24h: commodity avg `-0.8937` n `12`; crypto_alt avg `0.3937` n `229`; crypto_major avg `0.6809` n `8`; equity avg `0.6141` n `91`; fx avg `-0.1413` n `6`; index avg `0.2174` n `25`; metal avg `0.3713` n `20`; unknown avg `-0.0893` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
