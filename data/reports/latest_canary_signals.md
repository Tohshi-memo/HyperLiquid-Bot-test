# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T10:07:14.981369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.86` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0542` n `12`; crypto_alt avg `-0.206` n `228`; crypto_major avg `-0.2057` n `8`; equity avg `-0.0896` n `67`; fx avg `-0.0018` n `6`; index avg `-0.0225` n `23`; metal avg `0.077` n `18`; unknown avg `0.1341` n `396`
- 1h: commodity avg `0.0833` n `12`; crypto_alt avg `-0.0859` n `228`; crypto_major avg `0.1643` n `8`; equity avg `0.0101` n `67`; fx avg `-0.0015` n `6`; index avg `-0.0201` n `23`; metal avg `0.0418` n `18`; unknown avg `-1.1048` n `396`
- 4h: commodity avg `0.365` n `12`; crypto_alt avg `0.2447` n `228`; crypto_major avg `0.7246` n `8`; equity avg `0.0182` n `67`; fx avg `0.0035` n `6`; index avg `-0.0251` n `23`; metal avg `0.0277` n `18`; unknown avg `-0.8987` n `396`
- 24h: commodity avg `-2.6871` n `12`; crypto_alt avg `3.9394` n `228`; crypto_major avg `4.7384` n `8`; equity avg `2.658` n `67`; fx avg `0.0694` n `6`; index avg `1.3847` n `23`; metal avg `1.3751` n `18`; unknown avg `1.2473` n `386`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
