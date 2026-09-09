# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T05:07:29.659161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.1091` n `233`; crypto_major avg `-0.1794` n `8`; equity avg `0.0021` n `134`; fx avg `-0.0256` n `6`; index avg `-0.0066` n `26`; metal avg `0.0374` n `20`; unknown avg `0.1381` n `796`
- 1h: commodity avg `-0.0628` n `12`; crypto_alt avg `0.4739` n `233`; crypto_major avg `0.3038` n `8`; equity avg `0.1307` n `134`; fx avg `-0.0226` n `6`; index avg `0.017` n `26`; metal avg `0.07` n `20`; unknown avg `0.2541` n `790`
- 4h: commodity avg `-0.1204` n `12`; crypto_alt avg `0.4156` n `233`; crypto_major avg `0.3265` n `8`; equity avg `-0.0087` n `134`; fx avg `-0.0684` n `6`; index avg `-0.0121` n `26`; metal avg `0.0486` n `20`; unknown avg `0.0743` n `785`
- 24h: commodity avg `-0.0528` n `12`; crypto_alt avg `0.0254` n `232`; crypto_major avg `1.1726` n `8`; equity avg `0.4953` n `134`; fx avg `-0.0358` n `6`; index avg `-0.1289` n `26`; metal avg `-0.342` n `20`; unknown avg `1.5132` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
