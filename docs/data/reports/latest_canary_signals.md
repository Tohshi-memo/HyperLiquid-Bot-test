# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T17:39:46.950572+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0182` n `230`; crypto_major avg `-0.0399` n `8`; equity avg `-0.0131` n `114`; fx avg `-0.0112` n `6`; index avg `-0.0016` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.0462` n `791`
- 1h: commodity avg `0.0215` n `12`; crypto_alt avg `-0.1601` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `-0.0011` n `114`; fx avg `-0.0149` n `6`; index avg `-0.0084` n `25`; metal avg `0.0095` n `20`; unknown avg `0.2338` n `791`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `0.0372` n `230`; crypto_major avg `0.2568` n `8`; equity avg `0.1256` n `114`; fx avg `-0.0019` n `6`; index avg `-0.0093` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0388` n `791`
- 24h: commodity avg `0.0431` n `12`; crypto_alt avg `-0.2856` n `230`; crypto_major avg `0.1287` n `8`; equity avg `0.3166` n `114`; fx avg `-0.0109` n `6`; index avg `0.0225` n `25`; metal avg `0.0574` n `20`; unknown avg `0.1292` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2145`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
