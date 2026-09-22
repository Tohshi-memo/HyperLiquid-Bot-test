# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T19:52:29.441953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.07` n `12`; crypto_alt avg `0.0379` n `234`; crypto_major avg `-0.0356` n `8`; equity avg `0.0557` n `140`; fx avg `-0.006` n `6`; index avg `-0.0012` n `26`; metal avg `-0.0238` n `20`; unknown avg `8.2284` n `942`
- 1h: commodity avg `-0.1614` n `12`; crypto_alt avg `0.2189` n `234`; crypto_major avg `-0.0965` n `8`; equity avg `0.2339` n `140`; fx avg `-0.0136` n `6`; index avg `0.0541` n `26`; metal avg `0.1183` n `20`; unknown avg `6.928` n `940`
- 4h: commodity avg `-0.1783` n `12`; crypto_alt avg `0.7876` n `234`; crypto_major avg `0.1768` n `8`; equity avg `0.66` n `140`; fx avg `-0.0009` n `6`; index avg `0.1451` n `26`; metal avg `0.4577` n `20`; unknown avg `1.9942` n `888`
- 24h: commodity avg `0.057` n `12`; crypto_alt avg `2.1682` n `234`; crypto_major avg `1.0359` n `8`; equity avg `1.0276` n `140`; fx avg `-0.2903` n `6`; index avg `0.1391` n `26`; metal avg `0.3547` n `20`; unknown avg `1.2074` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
