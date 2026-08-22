# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T02:37:29.913179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `12`; crypto_alt avg `0.3158` n `230`; crypto_major avg `0.2395` n `8`; equity avg `-0.025` n `121`; fx avg `0.0047` n `6`; index avg `0.0006` n `25`; metal avg `-0.0022` n `20`; unknown avg `-0.2391` n `793`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `1.161` n `230`; crypto_major avg `1.0186` n `8`; equity avg `0.0241` n `121`; fx avg `0.0132` n `6`; index avg `0.0015` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.1556` n `793`
- 4h: commodity avg `-0.0446` n `12`; crypto_alt avg `2.2249` n `230`; crypto_major avg `1.394` n `8`; equity avg `-0.0003` n `121`; fx avg `0.0145` n `6`; index avg `0.0073` n `25`; metal avg `-0.0207` n `20`; unknown avg `-0.2196` n `793`
- 24h: commodity avg `0.0165` n `12`; crypto_alt avg `10.1` n `230`; crypto_major avg `7.6132` n `8`; equity avg `-0.0186` n `121`; fx avg `0.0533` n `6`; index avg `-0.0208` n `25`; metal avg `0.233` n `20`; unknown avg `1.3064` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
