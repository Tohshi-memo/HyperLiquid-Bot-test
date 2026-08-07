# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T20:37:38.535019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `-0.1046` n `230`; crypto_major avg `-0.0753` n `8`; equity avg `0.0258` n `112`; fx avg `0.0078` n `6`; index avg `0.0126` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.1432` n `782`
- 1h: commodity avg `0.0649` n `12`; crypto_alt avg `-0.2846` n `230`; crypto_major avg `-0.0486` n `8`; equity avg `0.2651` n `112`; fx avg `0.0073` n `6`; index avg `0.0198` n `25`; metal avg `-0.1067` n `20`; unknown avg `0.0214` n `782`
- 4h: commodity avg `-0.2736` n `12`; crypto_alt avg `-0.43` n `230`; crypto_major avg `-0.2315` n `8`; equity avg `0.3878` n `112`; fx avg `0.0015` n `6`; index avg `0.064` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.1672` n `782`
- 24h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.2384` n `230`; crypto_major avg `-0.0121` n `8`; equity avg `2.096` n `112`; fx avg `-0.1501` n `6`; index avg `0.1165` n `25`; metal avg `0.3198` n `20`; unknown avg `0.0268` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0533`, n `668`, weak_sample_signal
