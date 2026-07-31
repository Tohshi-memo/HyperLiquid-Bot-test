# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T06:07:32.361027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0823` n `12`; crypto_alt avg `0.0868` n `230`; crypto_major avg `0.1318` n `8`; equity avg `0.1677` n `102`; fx avg `-0.063` n `6`; index avg `0.0201` n `25`; metal avg `0.0875` n `20`; unknown avg `0.0048` n `747`
- 1h: commodity avg `0.0131` n `12`; crypto_alt avg `0.1124` n `230`; crypto_major avg `0.0072` n `8`; equity avg `0.2187` n `102`; fx avg `-0.0357` n `6`; index avg `0.0734` n `25`; metal avg `-0.0461` n `20`; unknown avg `-0.0084` n `747`
- 4h: commodity avg `0.0402` n `12`; crypto_alt avg `-0.2314` n `230`; crypto_major avg `-0.1763` n `8`; equity avg `0.8469` n `102`; fx avg `-0.016` n `6`; index avg `0.1784` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0165` n `747`
- 24h: commodity avg `-0.5329` n `12`; crypto_alt avg `0.118` n `230`; crypto_major avg `0.931` n `8`; equity avg `9.0007` n `102`; fx avg `-0.1266` n `6`; index avg `1.3201` n `25`; metal avg `0.6957` n `20`; unknown avg `0.0576` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
