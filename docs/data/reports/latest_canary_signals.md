# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T12:22:28.790187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0835` n `13`; crypto_alt avg `-0.0792` n `235`; crypto_major avg `-0.0831` n `8`; equity avg `-0.0361` n `150`; fx avg `0.0144` n `6`; index avg `-0.0042` n `26`; metal avg `-0.0164` n `20`; unknown avg `0.0075` n `1074`
- 1h: commodity avg `-0.1384` n `13`; crypto_alt avg `-0.1116` n `235`; crypto_major avg `-0.0464` n `8`; equity avg `0.0599` n `150`; fx avg `0.0404` n `6`; index avg `0.0301` n `26`; metal avg `0.0421` n `20`; unknown avg `0.7923` n `1066`
- 4h: commodity avg `-0.508` n `13`; crypto_alt avg `0.3458` n `235`; crypto_major avg `0.341` n `8`; equity avg `0.3947` n `149`; fx avg `0.1062` n `6`; index avg `0.106` n `26`; metal avg `0.1052` n `20`; unknown avg `0.8016` n `1066`
- 24h: commodity avg `-0.8651` n `13`; crypto_alt avg `-0.478` n `235`; crypto_major avg `-0.0913` n `8`; equity avg `0.8681` n `149`; fx avg `0.1172` n `6`; index avg `0.2764` n `26`; metal avg `-0.0581` n `20`; unknown avg `-0.2659` n `876`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
