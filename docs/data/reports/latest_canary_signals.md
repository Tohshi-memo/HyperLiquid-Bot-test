# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T22:37:35.113752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.1272` n `230`; crypto_major avg `-0.0901` n `8`; equity avg `0.0121` n `112`; fx avg `0.0035` n `6`; index avg `0.0013` n `25`; metal avg `0.0144` n `20`; unknown avg `0.127` n `782`
- 1h: commodity avg `-0.0741` n `12`; crypto_alt avg `-0.2292` n `230`; crypto_major avg `-0.1508` n `8`; equity avg `0.036` n `112`; fx avg `0.0129` n `6`; index avg `0.0066` n `25`; metal avg `0.0364` n `20`; unknown avg `0.0076` n `782`
- 4h: commodity avg `-0.3094` n `12`; crypto_alt avg `-0.3273` n `230`; crypto_major avg `0.1126` n `8`; equity avg `0.5089` n `112`; fx avg `0.0207` n `6`; index avg `0.0948` n `25`; metal avg `0.0841` n `20`; unknown avg `-0.1225` n `782`
- 24h: commodity avg `-0.2103` n `12`; crypto_alt avg `-0.56` n `230`; crypto_major avg `-0.2468` n `8`; equity avg `1.7033` n `112`; fx avg `-0.1217` n `6`; index avg `0.0985` n `25`; metal avg `0.4943` n `20`; unknown avg `0.0951` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
