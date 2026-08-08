# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T02:18:00.113891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `12`; crypto_alt avg `0.027` n `230`; crypto_major avg `-0.0572` n `8`; equity avg `-0.0283` n `112`; fx avg `0.001` n `6`; index avg `-0.0` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.0865` n `783`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `0.1571` n `230`; crypto_major avg `0.0344` n `8`; equity avg `0.0909` n `112`; fx avg `0.0018` n `6`; index avg `0.0277` n `25`; metal avg `-0.055` n `20`; unknown avg `-0.2095` n `783`
- 4h: commodity avg `0.0184` n `12`; crypto_alt avg `0.2124` n `230`; crypto_major avg `0.12` n `8`; equity avg `0.2056` n `112`; fx avg `0.0058` n `6`; index avg `0.0008` n `25`; metal avg `0.0134` n `20`; unknown avg `-0.2598` n `782`
- 24h: commodity avg `-0.1894` n `12`; crypto_alt avg `-0.4734` n `230`; crypto_major avg `0.1046` n `8`; equity avg `1.9067` n `112`; fx avg `-0.0573` n `6`; index avg `0.2233` n `25`; metal avg `0.3284` n `20`; unknown avg `-0.0814` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
