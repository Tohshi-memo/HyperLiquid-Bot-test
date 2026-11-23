# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T13:37:29.421212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `0.0406` n `239`; crypto_major avg `-0.0707` n `8`; equity avg `-0.1309` n `166`; fx avg `-0.0124` n `6`; index avg `-0.022` n `27`; metal avg `-0.0846` n `20`; unknown avg `158.1562` n `1266`
- 1h: commodity avg `-0.0526` n `13`; crypto_alt avg `-0.0234` n `239`; crypto_major avg `0.1001` n `8`; equity avg `0.2437` n `166`; fx avg `-0.0402` n `6`; index avg `0.0635` n `27`; metal avg `-0.0616` n `20`; unknown avg `0.1668` n `1258`
- 4h: commodity avg `-0.2921` n `13`; crypto_alt avg `-0.1646` n `239`; crypto_major avg `-0.054` n `8`; equity avg `-0.5384` n `166`; fx avg `-0.0857` n `6`; index avg `-0.0418` n `27`; metal avg `-0.1466` n `20`; unknown avg `0.4117` n `1250`
- 24h: commodity avg `-1.0283` n `13`; crypto_alt avg `0.6293` n `239`; crypto_major avg `1.2174` n `8`; equity avg `1.6046` n `166`; fx avg `0.1201` n `6`; index avg `0.03` n `27`; metal avg `0.2886` n `20`; unknown avg `-0.0504` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
