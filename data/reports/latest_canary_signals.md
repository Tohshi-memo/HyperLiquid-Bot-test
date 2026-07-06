# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T04:37:25.478380+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `-0.1687` n `229`; crypto_major avg `-0.0955` n `8`; equity avg `0.1443` n `88`; fx avg `-0.0181` n `6`; index avg `0.0372` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0333` n `765`
- 1h: commodity avg `0.0391` n `12`; crypto_alt avg `-0.2728` n `229`; crypto_major avg `-0.0863` n `8`; equity avg `0.0929` n `88`; fx avg `-0.0152` n `6`; index avg `0.0339` n `25`; metal avg `-0.0761` n `20`; unknown avg `1.2415` n `765`
- 4h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.3648` n `229`; crypto_major avg `-0.4046` n `8`; equity avg `-0.6015` n `88`; fx avg `0.0064` n `6`; index avg `-0.1656` n `25`; metal avg `-0.3314` n `20`; unknown avg `-0.452` n `763`
- 24h: commodity avg `-0.2032` n `12`; crypto_alt avg `0.1572` n `229`; crypto_major avg `1.1065` n `8`; equity avg `-0.6764` n `88`; fx avg `0.0544` n `6`; index avg `-0.0297` n `25`; metal avg `-0.2438` n `20`; unknown avg `1.0081` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
