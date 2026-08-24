# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T21:52:32.895104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.1001` n `231`; crypto_major avg `0.0521` n `8`; equity avg `-0.0037` n `122`; fx avg `0.0061` n `6`; index avg `0.0009` n `25`; metal avg `0.0138` n `20`; unknown avg `0.0276` n `794`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `0.2405` n `231`; crypto_major avg `0.3375` n `8`; equity avg `0.0901` n `122`; fx avg `-0.0029` n `6`; index avg `0.0102` n `25`; metal avg `0.0315` n `20`; unknown avg `-0.0682` n `794`
- 4h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.6564` n `231`; crypto_major avg `0.7354` n `8`; equity avg `-0.0086` n `122`; fx avg `0.0022` n `6`; index avg `0.0272` n `25`; metal avg `0.1279` n `20`; unknown avg `-0.4052` n `794`
- 24h: commodity avg `-0.2039` n `12`; crypto_alt avg `-1.8444` n `231`; crypto_major avg `-1.0861` n `8`; equity avg `-2.8154` n `122`; fx avg `-0.0493` n `6`; index avg `-0.3629` n `25`; metal avg `0.1156` n `20`; unknown avg `0.7461` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
