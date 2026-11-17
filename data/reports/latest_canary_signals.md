# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T00:22:36.208532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.1075` n `239`; crypto_major avg `-0.2257` n `8`; equity avg `0.0734` n `162`; fx avg `-0.0052` n `6`; index avg `0.0234` n `27`; metal avg `-0.0214` n `20`; unknown avg `-0.2488` n `1264`
- 1h: commodity avg `-0.0336` n `13`; crypto_alt avg `-0.2557` n `239`; crypto_major avg `-0.7499` n `8`; equity avg `0.0558` n `162`; fx avg `0.0086` n `6`; index avg `-0.0026` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.3438` n `1258`
- 4h: commodity avg `-0.0718` n `13`; crypto_alt avg `-0.3296` n `239`; crypto_major avg `-0.3192` n `8`; equity avg `-0.1853` n `162`; fx avg `-0.0028` n `6`; index avg `-0.0177` n `27`; metal avg `-0.0072` n `20`; unknown avg `0.0919` n `1190`
- 24h: commodity avg `-1.0576` n `13`; crypto_alt avg `-0.5736` n `239`; crypto_major avg `-0.4573` n `8`; equity avg `-4.3489` n `162`; fx avg `-0.0969` n `6`; index avg `-0.4908` n `27`; metal avg `-0.6576` n `20`; unknown avg `504.3861` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
