# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T13:52:39.317082+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `13`; crypto_alt avg `-0.2167` n `237`; crypto_major avg `-0.2607` n `8`; equity avg `-0.2261` n `151`; fx avg `-0.0079` n `6`; index avg `-0.0474` n `26`; metal avg `-0.071` n `20`; unknown avg `0.0594` n `1195`
- 1h: commodity avg `-0.1226` n `13`; crypto_alt avg `-0.334` n `237`; crypto_major avg `-0.4775` n `8`; equity avg `-0.3267` n `151`; fx avg `0.0069` n `6`; index avg `-0.0281` n `26`; metal avg `-0.0545` n `20`; unknown avg `0.3191` n `1175`
- 4h: commodity avg `-0.1362` n `13`; crypto_alt avg `-0.62` n `237`; crypto_major avg `-0.8331` n `8`; equity avg `0.0607` n `151`; fx avg `0.0377` n `6`; index avg `-0.0115` n `26`; metal avg `-0.1465` n `20`; unknown avg `0.3047` n `1151`
- 24h: commodity avg `-0.341` n `13`; crypto_alt avg `0.2386` n `237`; crypto_major avg `0.9678` n `8`; equity avg `2.8975` n `151`; fx avg `-0.0186` n `6`; index avg `0.4924` n `26`; metal avg `0.107` n `20`; unknown avg `2.0417` n `949`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.205`, n `667`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1602`, n `667`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1366`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `667`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `667`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0599`, n `667`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
