# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T03:09:39.583914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0404` n `12`; crypto_alt avg `0.2277` n `230`; crypto_major avg `0.084` n `8`; equity avg `0.0032` n `114`; fx avg `0.0045` n `6`; index avg `-0.0032` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0754` n `791`
- 1h: commodity avg `-0.0152` n `12`; crypto_alt avg `0.2183` n `230`; crypto_major avg `0.1859` n `8`; equity avg `0.0422` n `114`; fx avg `0.004` n `6`; index avg `0.0024` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0028` n `791`
- 4h: commodity avg `0.0578` n `12`; crypto_alt avg `-0.2834` n `230`; crypto_major avg `0.0217` n `8`; equity avg `0.0584` n `114`; fx avg `0.0017` n `6`; index avg `0.0095` n `25`; metal avg `0.0185` n `20`; unknown avg `-0.0763` n `791`
- 24h: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.0546` n `230`; crypto_major avg `-0.0799` n `8`; equity avg `0.1977` n `114`; fx avg `-0.0495` n `6`; index avg `0.0103` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0108` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2233`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
