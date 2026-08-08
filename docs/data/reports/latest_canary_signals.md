# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T06:07:26.330758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.032` n `230`; crypto_major avg `0.0623` n `8`; equity avg `-0.0741` n `112`; fx avg `0.0057` n `6`; index avg `0.0004` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.0152` n `752`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `-0.0032` n `230`; crypto_major avg `0.0267` n `8`; equity avg `-0.0373` n `112`; fx avg `0.0081` n `6`; index avg `-0.0147` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0016` n `751`
- 4h: commodity avg `0.0172` n `12`; crypto_alt avg `0.2707` n `230`; crypto_major avg `0.3162` n `8`; equity avg `-0.2413` n `112`; fx avg `0.0062` n `6`; index avg `-0.0485` n `25`; metal avg `-0.0089` n `20`; unknown avg `0.1494` n `751`
- 24h: commodity avg `-0.2087` n `12`; crypto_alt avg `-0.2335` n `230`; crypto_major avg `0.7189` n `8`; equity avg `1.3335` n `112`; fx avg `-0.0796` n `6`; index avg `0.1165` n `25`; metal avg `0.1307` n `20`; unknown avg `0.0343` n `750`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
