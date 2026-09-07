# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T23:22:29.617131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0116` n `232`; crypto_major avg `-0.0699` n `8`; equity avg `-0.0248` n `134`; fx avg `-0.0168` n `6`; index avg `-0.0095` n `26`; metal avg `0.0144` n `20`; unknown avg `0.2841` n `797`
- 1h: commodity avg `0.0076` n `12`; crypto_alt avg `-0.149` n `232`; crypto_major avg `0.0254` n `8`; equity avg `-0.1649` n `134`; fx avg `-0.0405` n `6`; index avg `-0.0495` n `26`; metal avg `0.003` n `20`; unknown avg `0.3313` n `795`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `-0.124` n `232`; crypto_major avg `-0.0886` n `8`; equity avg `-0.181` n `134`; fx avg `-0.0335` n `6`; index avg `-0.0599` n `26`; metal avg `0.0242` n `20`; unknown avg `1.9353` n `752`
- 24h: commodity avg `0.2195` n `12`; crypto_alt avg `-0.5639` n `232`; crypto_major avg `-1.5509` n `8`; equity avg `0.275` n `134`; fx avg `-0.1834` n `6`; index avg `0.0538` n `26`; metal avg `0.0886` n `20`; unknown avg `7945.2999` n `642`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
