# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T11:52:33.318118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0268` n `13`; crypto_alt avg `0.0102` n `235`; crypto_major avg `0.1269` n `8`; equity avg `0.0597` n `150`; fx avg `0.01` n `6`; index avg `0.03` n `26`; metal avg `0.0499` n `20`; unknown avg `1.3361` n `1074`
- 1h: commodity avg `0.0288` n `13`; crypto_alt avg `0.0968` n `235`; crypto_major avg `0.1259` n `8`; equity avg `0.1904` n `150`; fx avg `0.0577` n `6`; index avg `0.0779` n `26`; metal avg `0.1248` n `20`; unknown avg `1.8396` n `1072`
- 4h: commodity avg `-0.3322` n `13`; crypto_alt avg `0.6564` n `235`; crypto_major avg `0.6664` n `8`; equity avg `0.456` n `149`; fx avg `0.0933` n `6`; index avg `0.1247` n `26`; metal avg `0.1868` n `20`; unknown avg `0.7804` n `1056`
- 24h: commodity avg `-0.6992` n `13`; crypto_alt avg `-0.4551` n `235`; crypto_major avg `-0.0725` n `8`; equity avg `0.8914` n `149`; fx avg `0.0686` n `6`; index avg `0.2839` n `26`; metal avg `0.0174` n `20`; unknown avg `-0.3495` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1746`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
