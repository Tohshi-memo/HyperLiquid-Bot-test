# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T01:22:18.223709+00:00`
- Correlation status: `ready`
- Asset price records: `505`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.73` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1866` n `12`; crypto_alt avg `-0.1442` n `228`; crypto_major avg `0.0245` n `8`; equity avg `0.1018` n `65`; fx avg `-0.0211` n `4`; index avg `0.0393` n `23`; metal avg `0.4054` n `18`; unknown avg `0.0029` n `357`
- 1h: commodity avg `-0.1343` n `12`; crypto_alt avg `-0.9988` n `228`; crypto_major avg `-0.599` n `8`; equity avg `-0.1418` n `65`; fx avg `0.0353` n `4`; index avg `0.0168` n `23`; metal avg `0.3895` n `18`; unknown avg `-0.1556` n `356`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-1.1087` n `228`; crypto_major avg `-0.8536` n `8`; equity avg `-0.228` n `65`; fx avg `0.0811` n `4`; index avg `0.0462` n `23`; metal avg `0.4156` n `18`; unknown avg `-0.1913` n `356`
- 24h: commodity avg `-1.9201` n `7`; crypto_alt avg `0.5722` n `223`; crypto_major avg `-0.6244` n `7`; equity avg `1.446` n `47`; fx avg `-0.2539` n `4`; index avg `0.8526` n `6`; metal avg `2.7758` n `7`; unknown avg `3.1867` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1311`, n `501`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `501`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `501`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `497`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0662`, n `501`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `497`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0628`, n `497`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `501`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.06`, n `497`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `497`, weak_sample_signal
