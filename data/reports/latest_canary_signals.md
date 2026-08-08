# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T00:22:34.098481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.0125` n `230`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0514` n `112`; fx avg `0.0033` n `6`; index avg `-0.0266` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0448` n `783`
- 1h: commodity avg `-0.0688` n `12`; crypto_alt avg `-0.0199` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `0.0975` n `112`; fx avg `-0.0051` n `6`; index avg `-0.027` n `25`; metal avg `0.0344` n `20`; unknown avg `-0.0143` n `783`
- 4h: commodity avg `-0.0913` n `12`; crypto_alt avg `-0.1757` n `230`; crypto_major avg `-0.2609` n `8`; equity avg `0.1738` n `112`; fx avg `0.0352` n `6`; index avg `-0.0138` n `25`; metal avg `0.1509` n `20`; unknown avg `-0.0821` n `782`
- 24h: commodity avg `-0.2522` n `12`; crypto_alt avg `-0.474` n `230`; crypto_major avg `-0.0291` n `8`; equity avg `2.0722` n `112`; fx avg `-0.1197` n `6`; index avg `0.1393` n `25`; metal avg `0.5253` n `20`; unknown avg `0.1066` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
