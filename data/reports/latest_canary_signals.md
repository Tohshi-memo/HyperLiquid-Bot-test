# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T02:22:28.911902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.0783` n `235`; crypto_major avg `-0.0287` n `8`; equity avg `0.0036` n `143`; fx avg `0.0025` n `6`; index avg `-0.0009` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.0679` n `1079`
- 1h: commodity avg `0.0179` n `13`; crypto_alt avg `-0.0961` n `235`; crypto_major avg `0.0601` n `8`; equity avg `0.0211` n `143`; fx avg `0.0013` n `6`; index avg `-0.0008` n `26`; metal avg `0.0022` n `20`; unknown avg `0.2783` n `1077`
- 4h: commodity avg `-0.0403` n `13`; crypto_alt avg `0.046` n `235`; crypto_major avg `0.0346` n `8`; equity avg `-0.0078` n `143`; fx avg `-0.0043` n `6`; index avg `-0.0103` n `26`; metal avg `0.0042` n `20`; unknown avg `0.075` n `1071`
- 24h: commodity avg `0.1713` n `13`; crypto_alt avg `1.1235` n `235`; crypto_major avg `0.4525` n `8`; equity avg `0.1163` n `143`; fx avg `-0.0288` n `6`; index avg `0.0033` n `26`; metal avg `-0.008` n `20`; unknown avg `-0.0367` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2008`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
