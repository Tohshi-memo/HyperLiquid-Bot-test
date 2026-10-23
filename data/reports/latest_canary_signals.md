# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T01:37:29.314668+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `13`; crypto_alt avg `-0.0723` n `237`; crypto_major avg `-0.2093` n `8`; equity avg `-0.0079` n `151`; fx avg `0.0224` n `6`; index avg `-0.0334` n `26`; metal avg `-0.061` n `20`; unknown avg `0.074` n `1233`
- 1h: commodity avg `0.0969` n `13`; crypto_alt avg `0.075` n `237`; crypto_major avg `-0.1314` n `8`; equity avg `0.3918` n `151`; fx avg `0.0348` n `6`; index avg `0.016` n `26`; metal avg `-0.0678` n `20`; unknown avg `0.4993` n `1231`
- 4h: commodity avg `0.0887` n `13`; crypto_alt avg `0.0734` n `237`; crypto_major avg `-0.0867` n `8`; equity avg `0.3568` n `151`; fx avg `-0.0541` n `6`; index avg `0.0033` n `26`; metal avg `-0.1518` n `20`; unknown avg `0.1146` n `1185`
- 24h: commodity avg `0.4202` n `13`; crypto_alt avg `-4.2043` n `237`; crypto_major avg `-2.8527` n `8`; equity avg `-4.1475` n `151`; fx avg `-0.2171` n `6`; index avg `-0.5099` n `26`; metal avg `-0.888` n `20`; unknown avg `58.026` n `905`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
