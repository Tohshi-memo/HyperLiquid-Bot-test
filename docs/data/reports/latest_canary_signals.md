# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:07:23.607451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `-0.034` n `231`; crypto_major avg `-0.02` n `8`; equity avg `-0.0216` n `122`; fx avg `-0.0079` n `6`; index avg `0.0088` n `25`; metal avg `-0.0085` n `20`; unknown avg `1.0985` n `793`
- 1h: commodity avg `0.0199` n `12`; crypto_alt avg `0.371` n `231`; crypto_major avg `0.3461` n `8`; equity avg `0.0553` n `122`; fx avg `0.0017` n `6`; index avg `0.0218` n `25`; metal avg `0.006` n `20`; unknown avg `0.0345` n `793`
- 4h: commodity avg `-0.0164` n `12`; crypto_alt avg `1.5719` n `231`; crypto_major avg `0.2658` n `8`; equity avg `0.157` n `122`; fx avg `-0.0037` n `6`; index avg `0.0424` n `25`; metal avg `0.0224` n `20`; unknown avg `1.1011` n `793`
- 24h: commodity avg `0.0239` n `12`; crypto_alt avg `2.0893` n `231`; crypto_major avg `1.0301` n `8`; equity avg `0.6555` n `122`; fx avg `0.0257` n `6`; index avg `0.0873` n `25`; metal avg `0.0829` n `20`; unknown avg `7.712` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
