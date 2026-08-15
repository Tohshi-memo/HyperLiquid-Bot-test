# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T18:22:24.947582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1061` n `230`; crypto_major avg `-0.1439` n `8`; equity avg `-0.0038` n `114`; fx avg `-0.0004` n `6`; index avg `0.0056` n `25`; metal avg `0.0081` n `20`; unknown avg `0.0148` n `791`
- 1h: commodity avg `0.0328` n `12`; crypto_alt avg `-0.2119` n `230`; crypto_major avg `-0.1062` n `8`; equity avg `0.0537` n `114`; fx avg `0.0022` n `6`; index avg `0.0086` n `25`; metal avg `0.0149` n `20`; unknown avg `-0.0287` n `791`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `0.199` n `230`; crypto_major avg `0.1481` n `8`; equity avg `0.0483` n `114`; fx avg `-0.0012` n `6`; index avg `0.011` n `25`; metal avg `0.0084` n `20`; unknown avg `5.0505` n `791`
- 24h: commodity avg `-0.0985` n `12`; crypto_alt avg `0.7201` n `230`; crypto_major avg `0.4125` n `8`; equity avg `0.3016` n `114`; fx avg `0.0392` n `6`; index avg `0.0329` n `25`; metal avg `0.0441` n `20`; unknown avg `-0.0289` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
