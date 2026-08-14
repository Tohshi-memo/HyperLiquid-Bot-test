# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T08:07:29.284706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0187` n `230`; crypto_major avg `0.0088` n `8`; equity avg `0.2482` n `113`; fx avg `-0.0108` n `6`; index avg `0.0198` n `25`; metal avg `-0.0557` n `20`; unknown avg `-0.0129` n `787`
- 1h: commodity avg `0.059` n `12`; crypto_alt avg `-0.1833` n `230`; crypto_major avg `0.0044` n `8`; equity avg `0.2941` n `113`; fx avg `-0.0319` n `6`; index avg `0.0274` n `25`; metal avg `0.05` n `20`; unknown avg `-0.0381` n `787`
- 4h: commodity avg `0.2783` n `12`; crypto_alt avg `-0.4352` n `230`; crypto_major avg `-0.4889` n `8`; equity avg `0.3008` n `113`; fx avg `0.0144` n `6`; index avg `0.0569` n `25`; metal avg `0.1376` n `20`; unknown avg `0.0454` n `755`
- 24h: commodity avg `0.0162` n `12`; crypto_alt avg `-0.7869` n `230`; crypto_major avg `-1.0377` n `8`; equity avg `1.6616` n `113`; fx avg `-0.0578` n `6`; index avg `0.3221` n `25`; metal avg `-0.0658` n `20`; unknown avg `1.0338` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1829`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
