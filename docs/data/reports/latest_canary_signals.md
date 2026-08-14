# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T02:37:27.224909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `0.0133` n `8`; equity avg `0.1215` n `113`; fx avg `-0.0072` n `6`; index avg `0.0066` n `25`; metal avg `0.0723` n `20`; unknown avg `-0.051` n `787`
- 1h: commodity avg `0.0212` n `12`; crypto_alt avg `-0.01` n `230`; crypto_major avg `-0.0109` n `8`; equity avg `0.1644` n `113`; fx avg `-0.011` n `6`; index avg `0.045` n `25`; metal avg `0.0424` n `20`; unknown avg `-0.0762` n `787`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `-0.1515` n `8`; equity avg `-0.2614` n `113`; fx avg `-0.046` n `6`; index avg `-0.0449` n `25`; metal avg `-0.1653` n `20`; unknown avg `0.6884` n `787`
- 24h: commodity avg `-0.3038` n `12`; crypto_alt avg `0.4249` n `230`; crypto_major avg `0.4992` n `8`; equity avg `0.9799` n `113`; fx avg `0.0027` n `6`; index avg `0.2453` n `25`; metal avg `-0.5316` n `20`; unknown avg `1.1215` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2455`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1866`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
