# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T12:07:31.813579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1105` n `13`; crypto_alt avg `-0.1693` n `239`; crypto_major avg `-0.2782` n `8`; equity avg `0.1449` n `161`; fx avg `0.0003` n `6`; index avg `0.0098` n `27`; metal avg `-0.0059` n `20`; unknown avg `19.1303` n `1251`
- 1h: commodity avg `0.0828` n `13`; crypto_alt avg `0.0993` n `239`; crypto_major avg `-0.209` n `8`; equity avg `0.2206` n `161`; fx avg `-0.002` n `6`; index avg `0.0238` n `27`; metal avg `-0.072` n `20`; unknown avg `19.4372` n `1249`
- 4h: commodity avg `0.3409` n `13`; crypto_alt avg `0.2106` n `239`; crypto_major avg `-0.1313` n `8`; equity avg `0.6073` n `161`; fx avg `-0.0377` n `6`; index avg `0.0254` n `27`; metal avg `0.0301` n `20`; unknown avg `40.8625` n `1233`
- 24h: commodity avg `0.8696` n `13`; crypto_alt avg `-0.4544` n `239`; crypto_major avg `-1.3168` n `8`; equity avg `3.0468` n `161`; fx avg `-0.2195` n `6`; index avg `0.2826` n `27`; metal avg `0.1985` n `20`; unknown avg `1.2814` n `1173`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
