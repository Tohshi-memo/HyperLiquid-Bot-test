# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T15:37:29.807079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.331` n `230`; crypto_major avg `0.3161` n `8`; equity avg `-0.0853` n `114`; fx avg `0.0229` n `6`; index avg `-0.0261` n `25`; metal avg `0.0151` n `20`; unknown avg `0.1714` n `791`
- 1h: commodity avg `0.0303` n `12`; crypto_alt avg `0.1308` n `230`; crypto_major avg `0.35` n `8`; equity avg `-0.7064` n `114`; fx avg `0.0549` n `6`; index avg `-0.0992` n `25`; metal avg `-0.0434` n `20`; unknown avg `0.1364` n `787`
- 4h: commodity avg `0.1479` n `12`; crypto_alt avg `0.0481` n `230`; crypto_major avg `0.047` n `8`; equity avg `-0.9672` n `114`; fx avg `0.08` n `6`; index avg `-0.1766` n `25`; metal avg `0.0886` n `20`; unknown avg `-0.237` n `786`
- 24h: commodity avg `-0.0372` n `12`; crypto_alt avg `-0.792` n `230`; crypto_major avg `-0.804` n `8`; equity avg `-0.6154` n `114`; fx avg `0.065` n `6`; index avg `-0.0662` n `25`; metal avg `0.1476` n `20`; unknown avg `0.273` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
