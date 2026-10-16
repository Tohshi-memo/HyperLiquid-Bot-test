# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T02:07:23.396541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1418` n `236`; crypto_major avg `-0.0675` n `8`; equity avg `-0.0686` n `151`; fx avg `-0.0111` n `6`; index avg `-0.0297` n `26`; metal avg `0.0129` n `20`; unknown avg `-0.1522` n `1134`
- 1h: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.6061` n `236`; crypto_major avg `-0.3377` n `8`; equity avg `-0.0663` n `151`; fx avg `-0.0177` n `6`; index avg `-0.0295` n `26`; metal avg `0.039` n `20`; unknown avg `-0.021` n `1134`
- 4h: commodity avg `-0.0826` n `13`; crypto_alt avg `-0.601` n `236`; crypto_major avg `-0.6908` n `8`; equity avg `-0.4144` n `151`; fx avg `0.0416` n `6`; index avg `-0.0793` n `26`; metal avg `-0.0743` n `20`; unknown avg `0.2702` n `1112`
- 24h: commodity avg `-0.0187` n `13`; crypto_alt avg `0.9925` n `236`; crypto_major avg `0.472` n `8`; equity avg `1.4905` n `151`; fx avg `-0.0024` n `6`; index avg `0.2479` n `26`; metal avg `0.2817` n `20`; unknown avg `25.4248` n `910`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0958`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0851`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0771`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0663`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0632`, n `666`, weak_sample_signal
