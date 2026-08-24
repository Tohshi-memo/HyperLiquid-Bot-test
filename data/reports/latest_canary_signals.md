# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:41:33.223981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.2588` n `231`; crypto_major avg `0.2963` n `8`; equity avg `-0.06` n `122`; fx avg `0.0027` n `6`; index avg `-0.0154` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0712` n `794`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `0.0431` n `231`; crypto_major avg `0.3724` n `8`; equity avg `-0.0918` n `122`; fx avg `0.007` n `6`; index avg `-0.0165` n `25`; metal avg `0.096` n `20`; unknown avg `0.1545` n `794`
- 4h: commodity avg `-0.0556` n `12`; crypto_alt avg `0.1022` n `231`; crypto_major avg `0.5853` n `8`; equity avg `-0.1764` n `122`; fx avg `-0.0041` n `6`; index avg `-0.0398` n `25`; metal avg `0.207` n `20`; unknown avg `-0.116` n `794`
- 24h: commodity avg `-0.1149` n `12`; crypto_alt avg `-1.4617` n `231`; crypto_major avg `-0.5997` n `8`; equity avg `-3.0293` n `122`; fx avg `-0.0562` n `6`; index avg `-0.3987` n `25`; metal avg `0.2709` n `20`; unknown avg `0.8305` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
