# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T03:07:26.061812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3111` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0318` n `12`; crypto_alt avg `0.3089` n `231`; crypto_major avg `0.1614` n `8`; equity avg `0.2001` n `128`; fx avg `-0.0077` n `6`; index avg `0.0602` n `26`; metal avg `0.0375` n `20`; unknown avg `0.3053` n `791`
- 1h: commodity avg `-0.0805` n `12`; crypto_alt avg `0.2533` n `231`; crypto_major avg `-0.1219` n `8`; equity avg `-0.0712` n `128`; fx avg `-0.0154` n `6`; index avg `0.0404` n `26`; metal avg `-0.025` n `20`; unknown avg `-0.0369` n `791`
- 4h: commodity avg `0.0725` n `12`; crypto_alt avg `-1.001` n `231`; crypto_major avg `-1.4276` n `8`; equity avg `-0.7582` n `128`; fx avg `-0.0602` n `6`; index avg `-0.1165` n `26`; metal avg `-0.3668` n `20`; unknown avg `2.3471` n `779`
- 24h: commodity avg `0.3565` n `12`; crypto_alt avg `-0.5594` n `231`; crypto_major avg `-2.2082` n `8`; equity avg `-1.2232` n `128`; fx avg `-0.043` n `6`; index avg `-0.2363` n `26`; metal avg `-0.3769` n `20`; unknown avg `-0.3842` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
