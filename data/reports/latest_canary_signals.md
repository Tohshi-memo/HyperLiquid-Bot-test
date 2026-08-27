# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T01:37:28.612396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0509` n `12`; crypto_alt avg `0.2772` n `231`; crypto_major avg `0.4145` n `8`; equity avg `0.2064` n `126`; fx avg `0.0041` n `6`; index avg `0.0527` n `25`; metal avg `0.0072` n `20`; unknown avg `1.4982` n `793`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.0347` n `231`; crypto_major avg `0.321` n `8`; equity avg `0.1483` n `126`; fx avg `-0.0084` n `6`; index avg `0.0027` n `25`; metal avg `0.1006` n `20`; unknown avg `1.3587` n `793`
- 4h: commodity avg `0.013` n `12`; crypto_alt avg `0.9431` n `231`; crypto_major avg `0.886` n `8`; equity avg `-0.0752` n `126`; fx avg `-0.084` n `6`; index avg `-0.0665` n `25`; metal avg `0.2128` n `20`; unknown avg `0.0446` n `793`
- 24h: commodity avg `0.4537` n `12`; crypto_alt avg `0.8913` n `231`; crypto_major avg `0.8647` n `8`; equity avg `1.6842` n `125`; fx avg `-0.1432` n `6`; index avg `0.3135` n `25`; metal avg `-0.1299` n `20`; unknown avg `0.9396` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
