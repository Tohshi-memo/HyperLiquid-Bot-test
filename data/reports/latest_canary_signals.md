# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T14:52:25.242239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.1328` n `230`; crypto_major avg `0.0457` n `8`; equity avg `-0.0089` n `114`; fx avg `0.0018` n `6`; index avg `0.0036` n `25`; metal avg `-0.0017` n `20`; unknown avg `-0.0307` n `791`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `0.1506` n `230`; crypto_major avg `-0.013` n `8`; equity avg `0.004` n `114`; fx avg `-0.0074` n `6`; index avg `-0.0057` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.038` n `791`
- 4h: commodity avg `0.06` n `12`; crypto_alt avg `0.2067` n `230`; crypto_major avg `0.1091` n `8`; equity avg `0.0485` n `114`; fx avg `-0.0358` n `6`; index avg `0.017` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.105` n `791`
- 24h: commodity avg `-0.1091` n `12`; crypto_alt avg `1.4213` n `230`; crypto_major avg `0.6081` n `8`; equity avg `-0.2499` n `114`; fx avg `0.0754` n `6`; index avg `-0.0588` n `25`; metal avg `0.0059` n `20`; unknown avg `-0.0034` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1857`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1437`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
