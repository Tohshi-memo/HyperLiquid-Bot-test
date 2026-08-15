# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T05:36:56.644073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `-0.1452` n `8`; equity avg `-0.0213` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0055` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.2012` n `791`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `0.2766` n `230`; crypto_major avg `-0.2044` n `8`; equity avg `-0.0591` n `114`; fx avg `0.0005` n `6`; index avg `-0.0115` n `25`; metal avg `0.0021` n `20`; unknown avg `-0.3546` n `791`
- 4h: commodity avg `0.1018` n `12`; crypto_alt avg `0.4895` n `230`; crypto_major avg `-0.0386` n `8`; equity avg `0.0142` n `114`; fx avg `0.0602` n `6`; index avg `-0.0158` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.24` n `791`
- 24h: commodity avg `0.1386` n `12`; crypto_alt avg `0.9459` n `230`; crypto_major avg `-0.4035` n `8`; equity avg `-0.0919` n `114`; fx avg `0.1706` n `6`; index avg `-0.0601` n `25`; metal avg `0.4327` n `20`; unknown avg `-0.1601` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
