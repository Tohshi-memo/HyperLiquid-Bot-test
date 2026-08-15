# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T20:52:26.297798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `0.047` n `8`; equity avg `-0.0073` n `114`; fx avg `-0.0055` n `6`; index avg `-0.0115` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.1631` n `791`
- 1h: commodity avg `-0.0552` n `12`; crypto_alt avg `-0.159` n `230`; crypto_major avg `-0.0886` n `8`; equity avg `-0.0099` n `114`; fx avg `-0.0025` n `6`; index avg `-0.0208` n `25`; metal avg `-0.007` n `20`; unknown avg `0.1261` n `791`
- 4h: commodity avg `0.0681` n `12`; crypto_alt avg `-0.1628` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `0.0982` n `114`; fx avg `-0.004` n `6`; index avg `-0.0157` n `25`; metal avg `0.0087` n `20`; unknown avg `1.04` n `791`
- 24h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.8675` n `230`; crypto_major avg `0.673` n `8`; equity avg `0.191` n `114`; fx avg `0.0027` n `6`; index avg `-0.0126` n `25`; metal avg `0.0468` n `20`; unknown avg `0.2204` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.2`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1789`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
