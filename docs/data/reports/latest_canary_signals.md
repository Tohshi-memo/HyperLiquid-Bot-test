# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T09:37:40.106446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.1692` n `235`; crypto_major avg `0.0298` n `8`; equity avg `0.0318` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0377` n `20`; unknown avg `0.5831` n `1078`
- 1h: commodity avg `0.0403` n `13`; crypto_alt avg `-0.1603` n `235`; crypto_major avg `0.073` n `8`; equity avg `-0.0932` n `150`; fx avg `-0.0322` n `6`; index avg `-0.0176` n `26`; metal avg `-0.0936` n `20`; unknown avg `0.7651` n `1076`
- 4h: commodity avg `-0.0041` n `13`; crypto_alt avg `-0.1109` n `235`; crypto_major avg `-0.068` n `8`; equity avg `0.187` n `150`; fx avg `-0.0195` n `6`; index avg `0.0404` n `26`; metal avg `-0.0895` n `20`; unknown avg `2.5545` n `988`
- 24h: commodity avg `-0.3336` n `13`; crypto_alt avg `-1.8781` n `235`; crypto_major avg `-2.1394` n `8`; equity avg `-0.5792` n `150`; fx avg `0.0786` n `6`; index avg `0.0369` n `26`; metal avg `0.4212` n `20`; unknown avg `7.9326` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
