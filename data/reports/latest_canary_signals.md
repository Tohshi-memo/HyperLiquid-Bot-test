# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T02:07:29.341766+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0573` n `232`; crypto_major avg `-0.057` n `8`; equity avg `0.0281` n `134`; fx avg `-0.0437` n `6`; index avg `-0.007` n `26`; metal avg `-0.0332` n `20`; unknown avg `0.1423` n `789`
- 1h: commodity avg `-0.0412` n `12`; crypto_alt avg `0.2589` n `232`; crypto_major avg `0.0588` n `8`; equity avg `0.1021` n `134`; fx avg `-0.0822` n `6`; index avg `0.0467` n `26`; metal avg `0.0984` n `20`; unknown avg `1.5057` n `789`
- 4h: commodity avg `-0.1181` n `12`; crypto_alt avg `0.7685` n `232`; crypto_major avg `0.2891` n `8`; equity avg `0.3656` n `134`; fx avg `-0.2046` n `6`; index avg `0.0885` n `26`; metal avg `0.1923` n `20`; unknown avg `13.0562` n `783`
- 24h: commodity avg `0.0731` n `12`; crypto_alt avg `1.5871` n `232`; crypto_major avg `-0.3442` n `8`; equity avg `0.7064` n `134`; fx avg `-0.3144` n `6`; index avg `0.1526` n `26`; metal avg `0.3421` n `20`; unknown avg `7692.3403` n `650`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
