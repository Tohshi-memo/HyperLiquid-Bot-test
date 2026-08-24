# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T23:37:29.480987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `12`; crypto_alt avg `0.2247` n `231`; crypto_major avg `0.1364` n `8`; equity avg `-0.0629` n `122`; fx avg `-0.0031` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0053` n `20`; unknown avg `-0.0803` n `794`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `0.0094` n `231`; crypto_major avg `0.2125` n `8`; equity avg `-0.0947` n `122`; fx avg `0.0011` n `6`; index avg `-0.018` n `25`; metal avg `0.0754` n `20`; unknown avg `-0.0207` n `794`
- 4h: commodity avg `-0.063` n `12`; crypto_alt avg `0.0688` n `231`; crypto_major avg `0.4247` n `8`; equity avg `-0.1791` n `122`; fx avg `-0.01` n `6`; index avg `-0.0413` n `25`; metal avg `0.1863` n `20`; unknown avg `-0.1888` n `794`
- 24h: commodity avg `-0.1222` n `12`; crypto_alt avg `-1.4908` n `231`; crypto_major avg `-0.7538` n `8`; equity avg `-3.0316` n `122`; fx avg `-0.0621` n `6`; index avg `-0.4001` n `25`; metal avg `0.2502` n `20`; unknown avg `0.8179` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
