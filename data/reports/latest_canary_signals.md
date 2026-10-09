# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T13:22:28.623620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0858` n `13`; crypto_alt avg `-0.1856` n `235`; crypto_major avg `-0.1834` n `8`; equity avg `-0.041` n `150`; fx avg `-0.0069` n `6`; index avg `-0.0255` n `26`; metal avg `0.0392` n `20`; unknown avg `5.6566` n `1078`
- 1h: commodity avg `0.1649` n `13`; crypto_alt avg `-0.2318` n `235`; crypto_major avg `-0.3017` n `8`; equity avg `-0.0344` n `150`; fx avg `-0.0001` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0241` n `20`; unknown avg `4.384` n `1076`
- 4h: commodity avg `0.1737` n `13`; crypto_alt avg `-0.561` n `235`; crypto_major avg `-0.1705` n `8`; equity avg `0.0453` n `150`; fx avg `-0.0556` n `6`; index avg `-0.0429` n `26`; metal avg `-0.0286` n `20`; unknown avg `2.6792` n `1070`
- 24h: commodity avg `-0.2519` n `13`; crypto_alt avg `-1.2177` n `235`; crypto_major avg `-1.235` n `8`; equity avg `-0.3602` n `150`; fx avg `0.0318` n `6`; index avg `-0.0157` n `26`; metal avg `0.5522` n `20`; unknown avg `7.3871` n `949`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
