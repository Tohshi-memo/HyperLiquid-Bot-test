# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T21:04:12.505490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.036` n `13`; crypto_alt avg `-0.1686` n `235`; crypto_major avg `-0.109` n `8`; equity avg `0.0017` n `150`; fx avg `0.006` n `6`; index avg `0.0084` n `26`; metal avg `0.0091` n `20`; unknown avg `-0.0692` n `1068`
- 1h: commodity avg `0.0079` n `13`; crypto_alt avg `-0.1769` n `235`; crypto_major avg `-0.047` n `8`; equity avg `0.0862` n `150`; fx avg `-0.0017` n `6`; index avg `0.0247` n `26`; metal avg `-0.0223` n `20`; unknown avg `1.9171` n `1020`
- 4h: commodity avg `0.3238` n `13`; crypto_alt avg `-0.4021` n `235`; crypto_major avg `-0.2102` n `8`; equity avg `-0.1035` n `150`; fx avg `-0.0023` n `6`; index avg `-0.038` n `26`; metal avg `0.0295` n `20`; unknown avg `0.9245` n `1006`
- 24h: commodity avg `0.3101` n `13`; crypto_alt avg `-1.217` n `235`; crypto_major avg `-0.7828` n `8`; equity avg `0.4188` n `149`; fx avg `0.1042` n `6`; index avg `-0.0009` n `26`; metal avg `0.0491` n `20`; unknown avg `862.6908` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
