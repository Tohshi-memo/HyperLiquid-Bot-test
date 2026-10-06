# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T05:22:29.730902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `-0.0038` n `235`; crypto_major avg `-0.0766` n `8`; equity avg `-0.0247` n `149`; fx avg `-0.0026` n `6`; index avg `0.002` n `26`; metal avg `-0.0056` n `20`; unknown avg `-0.0907` n `1074`
- 1h: commodity avg `0.0877` n `13`; crypto_alt avg `0.1405` n `235`; crypto_major avg `-0.0053` n `8`; equity avg `0.0028` n `149`; fx avg `-0.0113` n `6`; index avg `0.0011` n `26`; metal avg `-0.0558` n `20`; unknown avg `4.7341` n `1068`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `-0.5527` n `235`; crypto_major avg `-0.463` n `8`; equity avg `-0.0429` n `149`; fx avg `-0.0246` n `6`; index avg `-0.0093` n `26`; metal avg `-0.1481` n `20`; unknown avg `0.9056` n `1062`
- 24h: commodity avg `0.0674` n `13`; crypto_alt avg `-0.2378` n `235`; crypto_major avg `0.319` n `8`; equity avg `0.2169` n `149`; fx avg `0.0178` n `6`; index avg `0.1468` n `26`; metal avg `-0.0524` n `20`; unknown avg `587.4049` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
