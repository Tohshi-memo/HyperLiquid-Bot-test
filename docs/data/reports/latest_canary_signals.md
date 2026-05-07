# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T04:37:15.883201+00:00`
- Correlation status: `ready`
- Asset price records: `518`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.42` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0461` n `12`; crypto_alt avg `0.2157` n `228`; crypto_major avg `0.0158` n `8`; equity avg `-0.0465` n `65`; fx avg `-0.004` n `4`; index avg `-0.005` n `23`; metal avg `-0.016` n `18`; unknown avg `0.0925` n `358`
- 1h: commodity avg `0.1278` n `12`; crypto_alt avg `0.5873` n `228`; crypto_major avg `0.1542` n `8`; equity avg `0.075` n `65`; fx avg `-0.0101` n `4`; index avg `-0.0118` n `23`; metal avg `-0.1352` n `18`; unknown avg `0.1106` n `358`
- 4h: commodity avg `-0.1484` n `12`; crypto_alt avg `-0.1005` n `228`; crypto_major avg `-0.5491` n `8`; equity avg `0.3839` n `65`; fx avg `0.0353` n `4`; index avg `0.1263` n `23`; metal avg `0.0515` n `18`; unknown avg `-0.3623` n `356`
- 24h: commodity avg `-1.6695` n `7`; crypto_alt avg `0.7636` n `223`; crypto_major avg `-1.0065` n `7`; equity avg `1.1801` n `47`; fx avg `-0.0738` n `4`; index avg `1.1209` n `6`; metal avg `1.3716` n `7`; unknown avg `1.7354` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `514`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1083`, n `514`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `514`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `514`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `510`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0752`, n `510`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.073`, n `510`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0697`, n `510`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0695`, n `510`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `514`, weak_sample_signal
