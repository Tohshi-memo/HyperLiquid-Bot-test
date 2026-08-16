# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T05:07:24.964696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0189` n `230`; crypto_major avg `-0.0478` n `8`; equity avg `-0.0285` n `114`; fx avg `-0.0013` n `6`; index avg `0.0001` n `25`; metal avg `0.0014` n `20`; unknown avg `0.1425` n `791`
- 1h: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.0247` n `230`; crypto_major avg `-0.0323` n `8`; equity avg `-0.0335` n `114`; fx avg `0.0005` n `6`; index avg `-0.0013` n `25`; metal avg `0.0009` n `20`; unknown avg `0.134` n `791`
- 4h: commodity avg `0.021` n `12`; crypto_alt avg `-0.1262` n `230`; crypto_major avg `0.0283` n `8`; equity avg `0.139` n `114`; fx avg `0.0009` n `6`; index avg `0.0093` n `25`; metal avg `0.011` n `20`; unknown avg `0.0407` n `791`
- 24h: commodity avg `-0.0773` n `12`; crypto_alt avg `-0.2442` n `230`; crypto_major avg `-0.1384` n `8`; equity avg `0.2332` n `114`; fx avg `-0.0098` n `6`; index avg `0.0294` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.0861` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2222`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1693`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
