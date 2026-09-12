# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T21:36:44.112607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0437` n `233`; crypto_major avg `0.0518` n `8`; equity avg `0.0046` n `136`; fx avg `0.0` n `6`; index avg `-0.0033` n `26`; metal avg `0.0026` n `20`; unknown avg `3.7883` n `838`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.1289` n `233`; crypto_major avg `-0.0116` n `8`; equity avg `0.0278` n `136`; fx avg `-0.0024` n `6`; index avg `0.0037` n `26`; metal avg `-0.006` n `20`; unknown avg `3.037` n `828`
- 4h: commodity avg `0.0049` n `12`; crypto_alt avg `-0.4038` n `233`; crypto_major avg `-0.3289` n `8`; equity avg `-0.282` n `136`; fx avg `-0.006` n `6`; index avg `-0.0345` n `26`; metal avg `-0.0183` n `20`; unknown avg `1.0653` n `782`
- 24h: commodity avg `-0.0839` n `12`; crypto_alt avg `0.9112` n `233`; crypto_major avg `-0.276` n `8`; equity avg `-0.2646` n `136`; fx avg `-0.014` n `6`; index avg `0.0024` n `26`; metal avg `-0.0179` n `20`; unknown avg `6.1698` n `728`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0448`, n `668`, weak_sample_signal
