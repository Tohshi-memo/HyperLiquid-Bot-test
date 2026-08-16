# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T22:37:24.627229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.1709` n `230`; crypto_major avg `-0.2353` n `8`; equity avg `-0.0196` n `114`; fx avg `-0.0104` n `6`; index avg `-0.001` n `25`; metal avg `0.0443` n `20`; unknown avg `-0.115` n `791`
- 1h: commodity avg `-0.1214` n `12`; crypto_alt avg `-0.4952` n `230`; crypto_major avg `-0.5339` n `8`; equity avg `-0.0383` n `114`; fx avg `-0.0155` n `6`; index avg `0.0269` n `25`; metal avg `0.0345` n `20`; unknown avg `-0.0525` n `791`
- 4h: commodity avg `-0.107` n `12`; crypto_alt avg `-0.8903` n `230`; crypto_major avg `-0.6823` n `8`; equity avg `0.0068` n `114`; fx avg `-0.0102` n `6`; index avg `0.0386` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.0088` n `791`
- 24h: commodity avg `-0.0458` n `12`; crypto_alt avg `-1.1536` n `230`; crypto_major avg `-0.7422` n `8`; equity avg `0.2499` n `114`; fx avg `-0.0157` n `6`; index avg `0.0628` n `25`; metal avg `0.0417` n `20`; unknown avg `-0.0207` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1676`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
