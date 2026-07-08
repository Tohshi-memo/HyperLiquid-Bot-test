# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T21:07:42.374798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0402` n `12`; crypto_alt avg `-0.1509` n `229`; crypto_major avg `-0.1373` n `8`; equity avg `-0.008` n `91`; fx avg `0.0077` n `6`; index avg `0.0003` n `25`; metal avg `0.012` n `20`; unknown avg `-0.0834` n `764`
- 1h: commodity avg `0.0904` n `12`; crypto_alt avg `-0.4674` n `229`; crypto_major avg `-0.3513` n `8`; equity avg `-0.146` n `91`; fx avg `0.0103` n `6`; index avg `-0.034` n `25`; metal avg `-0.0633` n `20`; unknown avg `-0.1659` n `764`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `-0.3941` n `229`; crypto_major avg `-0.1174` n `8`; equity avg `0.6629` n `91`; fx avg `-0.0208` n `6`; index avg `0.0459` n `25`; metal avg `0.0749` n `20`; unknown avg `0.9719` n `764`
- 24h: commodity avg `0.447` n `12`; crypto_alt avg `-2.6243` n `229`; crypto_major avg `-3.0752` n `8`; equity avg `0.7964` n `91`; fx avg `-0.0065` n `6`; index avg `-0.06` n `25`; metal avg `-0.8104` n `20`; unknown avg `0.0161` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
