# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T15:22:28.757300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.6545` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5141` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `0.3877` n `231`; crypto_major avg `0.4085` n `8`; equity avg `0.0994` n `122`; fx avg `0.0029` n `6`; index avg `-0.0025` n `25`; metal avg `0.0028` n `20`; unknown avg `-0.1353` n `793`
- 1h: commodity avg `-0.0677` n `12`; crypto_alt avg `0.7878` n `231`; crypto_major avg `0.6251` n `8`; equity avg `0.2117` n `122`; fx avg `-0.0025` n `6`; index avg `-0.0121` n `25`; metal avg `0.0698` n `20`; unknown avg `0.0118` n `793`
- 4h: commodity avg `-0.1114` n `12`; crypto_alt avg `1.59` n `231`; crypto_major avg `1.7759` n `8`; equity avg `-0.8786` n `122`; fx avg `0.0046` n `6`; index avg `-0.1768` n `25`; metal avg `0.2618` n `20`; unknown avg `0.912` n `793`
- 24h: commodity avg `-0.2076` n `12`; crypto_alt avg `0.8135` n `231`; crypto_major avg `1.6464` n `8`; equity avg `-2.6476` n `122`; fx avg `-0.1066` n `6`; index avg `-0.388` n `25`; metal avg `0.3607` n `20`; unknown avg `3.6468` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
