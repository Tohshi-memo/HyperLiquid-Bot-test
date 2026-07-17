# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T23:07:29.045279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `-0.1447` n `230`; crypto_major avg `-0.1235` n `8`; equity avg `-0.0268` n `96`; fx avg `-0.0014` n `6`; index avg `-0.0006` n `25`; metal avg `0.0052` n `20`; unknown avg `0.009` n `769`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `0.0712` n `230`; crypto_major avg `-0.1836` n `8`; equity avg `0.0537` n `96`; fx avg `-0.0056` n `6`; index avg `-0.0036` n `25`; metal avg `0.0306` n `20`; unknown avg `0.1052` n `769`
- 4h: commodity avg `0.209` n `12`; crypto_alt avg `-0.5455` n `230`; crypto_major avg `-0.3499` n `8`; equity avg `-0.4624` n `96`; fx avg `-0.0544` n `6`; index avg `-0.0876` n `25`; metal avg `0.0553` n `20`; unknown avg `0.0415` n `769`
- 24h: commodity avg `0.7489` n `12`; crypto_alt avg `-0.7611` n `230`; crypto_major avg `-0.8251` n `8`; equity avg `-1.0439` n `94`; fx avg `0.0457` n `6`; index avg `-0.2775` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0102` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
