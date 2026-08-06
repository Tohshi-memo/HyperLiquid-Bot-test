# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T11:22:27.332259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0283` n `12`; crypto_alt avg `0.2955` n `230`; crypto_major avg `0.246` n `8`; equity avg `0.2335` n `109`; fx avg `0.0019` n `6`; index avg `0.041` n `25`; metal avg `-0.019` n `20`; unknown avg `0.0869` n `781`
- 1h: commodity avg `0.0067` n `12`; crypto_alt avg `0.0136` n `230`; crypto_major avg `0.0493` n `8`; equity avg `-0.4279` n `109`; fx avg `0.0115` n `6`; index avg `-0.0613` n `25`; metal avg `-0.0616` n `20`; unknown avg `0.0539` n `781`
- 4h: commodity avg `0.0658` n `12`; crypto_alt avg `-0.3829` n `230`; crypto_major avg `-0.5327` n `8`; equity avg `-0.54` n `109`; fx avg `-0.0104` n `6`; index avg `-0.0806` n `25`; metal avg `0.0683` n `20`; unknown avg `108.1718` n `781`
- 24h: commodity avg `-0.1742` n `12`; crypto_alt avg `0.0119` n `230`; crypto_major avg `-0.4595` n `8`; equity avg `-1.8983` n `109`; fx avg `-0.0032` n `6`; index avg `-0.3965` n `25`; metal avg `0.3393` n `20`; unknown avg `113.0152` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
