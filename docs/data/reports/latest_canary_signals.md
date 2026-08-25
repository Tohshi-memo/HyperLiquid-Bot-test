# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T05:07:32.170615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.2588` n `231`; crypto_major avg `0.3503` n `8`; equity avg `0.1506` n `122`; fx avg `-0.0051` n `6`; index avg `0.016` n `25`; metal avg `0.0873` n `20`; unknown avg `0.4348` n `794`
- 1h: commodity avg `-0.0905` n `12`; crypto_alt avg `0.5001` n `231`; crypto_major avg `0.4075` n `8`; equity avg `0.223` n `122`; fx avg `-0.0286` n `6`; index avg `0.02` n `25`; metal avg `0.0127` n `20`; unknown avg `0.6888` n `794`
- 4h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.7124` n `231`; crypto_major avg `0.7838` n `8`; equity avg `0.9538` n `122`; fx avg `-0.0033` n `6`; index avg `0.1552` n `25`; metal avg `-0.3895` n `20`; unknown avg `1.1844` n `794`
- 24h: commodity avg `-0.0362` n `12`; crypto_alt avg `2.2191` n `231`; crypto_major avg `3.1199` n `8`; equity avg `-0.297` n `122`; fx avg `0.0092` n `6`; index avg `-0.0827` n `25`; metal avg `-0.1602` n `20`; unknown avg `0.5841` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
