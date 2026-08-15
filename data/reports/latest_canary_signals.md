# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T04:52:28.099086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `12`; crypto_alt avg `-0.0232` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `0.0102` n `114`; fx avg `-0.0006` n `6`; index avg `-0.0059` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.0505` n `791`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.1661` n `230`; crypto_major avg `0.0028` n `8`; equity avg `0.0261` n `114`; fx avg `-0.0062` n `6`; index avg `-0.0113` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.1147` n `791`
- 4h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.027` n `230`; crypto_major avg `0.2367` n `8`; equity avg `0.0919` n `114`; fx avg `0.0459` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0454` n `20`; unknown avg `0.3029` n `791`
- 24h: commodity avg `0.1776` n `12`; crypto_alt avg `0.4397` n `230`; crypto_major avg `-0.1916` n `8`; equity avg `-0.0541` n `114`; fx avg `0.1349` n `6`; index avg `-0.0388` n `25`; metal avg `0.42` n `20`; unknown avg `0.0802` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
