# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T10:52:21.907547+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.219` n `231`; crypto_major avg `0.1368` n `8`; equity avg `0.038` n `127`; fx avg `0.0007` n `6`; index avg `-0.0066` n `26`; metal avg `0.0571` n `20`; unknown avg `0.0123` n `792`
- 1h: commodity avg `0.0595` n `12`; crypto_alt avg `-0.8714` n `231`; crypto_major avg `-0.8231` n `8`; equity avg `-0.2103` n `127`; fx avg `-0.0085` n `6`; index avg `-0.0405` n `26`; metal avg `0.0048` n `20`; unknown avg `0.1088` n `792`
- 4h: commodity avg `0.2188` n `12`; crypto_alt avg `0.404` n `231`; crypto_major avg `0.9498` n `8`; equity avg `0.4971` n `127`; fx avg `-0.0152` n `6`; index avg `0.0335` n `26`; metal avg `-0.153` n `20`; unknown avg `0.1217` n `791`
- 24h: commodity avg `0.4922` n `12`; crypto_alt avg `0.6015` n `231`; crypto_major avg `1.0307` n `8`; equity avg `1.8238` n `127`; fx avg `-0.0774` n `6`; index avg `0.2769` n `26`; metal avg `-0.3889` n `20`; unknown avg `0.4227` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
