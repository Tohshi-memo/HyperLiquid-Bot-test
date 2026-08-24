# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T11:22:25.088385+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0625` n `12`; crypto_alt avg `0.3761` n `231`; crypto_major avg `0.2788` n `8`; equity avg `0.1235` n `122`; fx avg `-0.0001` n `6`; index avg `0.0111` n `25`; metal avg `0.0135` n `20`; unknown avg `0.066` n `793`
- 1h: commodity avg `0.1308` n `12`; crypto_alt avg `-0.117` n `231`; crypto_major avg `-0.0331` n `8`; equity avg `-0.2617` n `122`; fx avg `0.0205` n `6`; index avg `-0.044` n `25`; metal avg `-0.0205` n `20`; unknown avg `1.093` n `793`
- 4h: commodity avg `0.2058` n `12`; crypto_alt avg `0.049` n `231`; crypto_major avg `-0.2151` n `8`; equity avg `-0.2045` n `122`; fx avg `-0.0077` n `6`; index avg `-0.0259` n `25`; metal avg `-0.0856` n `20`; unknown avg `0.4341` n `793`
- 24h: commodity avg `-0.0855` n `12`; crypto_alt avg `0.9291` n `231`; crypto_major avg `0.0276` n `8`; equity avg `-1.6182` n `122`; fx avg `-0.1176` n `6`; index avg `-0.1672` n `25`; metal avg `0.1316` n `20`; unknown avg `5.076` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
