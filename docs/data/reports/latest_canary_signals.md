# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T14:52:34.401664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.1929` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.4196` n `231`; crypto_major avg `-0.5979` n `8`; equity avg `-0.0096` n `122`; fx avg `0.0077` n `6`; index avg `-0.006` n `25`; metal avg `-0.0989` n `20`; unknown avg `0.1588` n `793`
- 1h: commodity avg `-0.1187` n `12`; crypto_alt avg `1.0693` n `231`; crypto_major avg `1.0293` n `8`; equity avg `0.8109` n `122`; fx avg `0.0136` n `6`; index avg `0.0842` n `25`; metal avg `0.0206` n `20`; unknown avg `0.121` n `793`
- 4h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.9324` n `231`; crypto_major avg `1.2491` n `8`; equity avg `-0.9438` n `122`; fx avg `0.0136` n `6`; index avg `-0.1561` n `25`; metal avg `0.152` n `20`; unknown avg `0.9733` n `793`
- 24h: commodity avg `-0.1794` n `12`; crypto_alt avg `0.3911` n `231`; crypto_major avg `0.7388` n `8`; equity avg `-2.4901` n `122`; fx avg `-0.1049` n `6`; index avg `-0.3246` n `25`; metal avg `0.2715` n `20`; unknown avg `3.7343` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
