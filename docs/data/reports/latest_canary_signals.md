# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T19:52:21.587647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.0036` n `231`; crypto_major avg `0.041` n `8`; equity avg `-0.0194` n `122`; fx avg `-0.0468` n `6`; index avg `0.0014` n `25`; metal avg `0.003` n `20`; unknown avg `-0.047` n `793`
- 1h: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0216` n `231`; crypto_major avg `0.0042` n `8`; equity avg `0.0571` n `122`; fx avg `-0.0664` n `6`; index avg `0.009` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.1182` n `793`
- 4h: commodity avg `-0.0655` n `12`; crypto_alt avg `0.2259` n `231`; crypto_major avg `0.186` n `8`; equity avg `0.2557` n `122`; fx avg `-0.0628` n `6`; index avg `0.0609` n `25`; metal avg `0.0158` n `20`; unknown avg `0.5814` n `793`
- 24h: commodity avg `-0.0358` n `12`; crypto_alt avg `2.1494` n `231`; crypto_major avg `0.2231` n `8`; equity avg `0.7988` n `122`; fx avg `-0.0453` n `6`; index avg `0.1298` n `25`; metal avg `0.0816` n `20`; unknown avg `5.469` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
