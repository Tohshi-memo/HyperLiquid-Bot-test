# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T05:22:30.035182+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.1548` n `230`; crypto_major avg `-0.0322` n `8`; equity avg `-0.0598` n `113`; fx avg `-0.0056` n `6`; index avg `0.018` n `25`; metal avg `0.0013` n `20`; unknown avg `-0.1828` n `787`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `-0.2748` n `230`; crypto_major avg `-0.1746` n `8`; equity avg `-0.1721` n `113`; fx avg `-0.0011` n `6`; index avg `-0.0118` n `25`; metal avg `-0.077` n `20`; unknown avg `-0.3318` n `787`
- 4h: commodity avg `0.0136` n `12`; crypto_alt avg `-0.4367` n `230`; crypto_major avg `-0.3598` n `8`; equity avg `-0.2214` n `113`; fx avg `-0.0208` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0206` n `20`; unknown avg `-0.3187` n `787`
- 24h: commodity avg `-0.4097` n `12`; crypto_alt avg `-0.5787` n `230`; crypto_major avg `-0.5132` n `8`; equity avg `0.4642` n `113`; fx avg `0.0168` n `6`; index avg `0.1832` n `25`; metal avg `-0.6174` n `20`; unknown avg `0.8008` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1632`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
