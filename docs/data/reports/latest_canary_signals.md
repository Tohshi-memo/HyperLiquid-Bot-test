# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T10:52:29.610372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0367` n `12`; crypto_alt avg `-0.1441` n `232`; crypto_major avg `-0.0979` n `8`; equity avg `-0.0802` n `134`; fx avg `-0.0094` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.3312` n `797`
- 1h: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.3006` n `232`; crypto_major avg `-0.1582` n `8`; equity avg `-0.023` n `134`; fx avg `0.0079` n `6`; index avg `0.002` n `26`; metal avg `-0.0297` n `20`; unknown avg `0.8361` n `795`
- 4h: commodity avg `-0.0155` n `12`; crypto_alt avg `0.9843` n `232`; crypto_major avg `0.7604` n `8`; equity avg `0.1109` n `134`; fx avg `-0.0289` n `6`; index avg `0.0199` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.8268` n `787`
- 24h: commodity avg `0.3442` n `12`; crypto_alt avg `0.6138` n `232`; crypto_major avg `-0.6755` n `8`; equity avg `-0.2202` n `134`; fx avg `-0.1204` n `6`; index avg `-0.0579` n `26`; metal avg `0.1101` n `20`; unknown avg `7463.7254` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
