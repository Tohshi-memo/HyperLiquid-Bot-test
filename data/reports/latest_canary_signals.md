# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T15:19:48.764602+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5204` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0392` n `12`; crypto_alt avg `0.1955` n `231`; crypto_major avg `0.215` n `8`; equity avg `0.0361` n `122`; fx avg `-0.0003` n `6`; index avg `-0.0025` n `25`; metal avg `0.0174` n `20`; unknown avg `-0.0982` n `793`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `0.5938` n `231`; crypto_major avg `0.4308` n `8`; equity avg `0.1482` n `122`; fx avg `-0.0058` n `6`; index avg `-0.0121` n `25`; metal avg `0.0845` n `20`; unknown avg `0.1483` n `793`
- 4h: commodity avg `-0.0898` n `12`; crypto_alt avg `1.3959` n `231`; crypto_major avg `1.5791` n `8`; equity avg `-0.9413` n `122`; fx avg `0.0013` n `6`; index avg `-0.1768` n `25`; metal avg `0.2766` n `20`; unknown avg `0.8903` n `793`
- 24h: commodity avg `-0.1862` n `12`; crypto_alt avg `0.6253` n `231`; crypto_major avg `1.4498` n `8`; equity avg `-2.709` n `122`; fx avg `-0.1098` n `6`; index avg `-0.388` n `25`; metal avg `0.3755` n `20`; unknown avg `3.6198` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
