# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T02:06:26.244076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5466` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0447` n `12`; crypto_alt avg `0.0732` n `231`; crypto_major avg `0.1841` n `8`; equity avg `0.0226` n `122`; fx avg `-0.0069` n `6`; index avg `-0.022` n `25`; metal avg `-0.2122` n `20`; unknown avg `-0.1167` n `794`
- 1h: commodity avg `0.1263` n `12`; crypto_alt avg `-0.3572` n `231`; crypto_major avg `-0.2351` n `8`; equity avg `0.2465` n `122`; fx avg `0.0131` n `6`; index avg `0.0251` n `25`; metal avg `-0.3102` n `20`; unknown avg `-0.2182` n `794`
- 4h: commodity avg `0.1352` n `12`; crypto_alt avg `0.5771` n `231`; crypto_major avg `1.3641` n `8`; equity avg `0.1885` n `122`; fx avg `0.0253` n `6`; index avg `-0.021` n `25`; metal avg `-0.1825` n `20`; unknown avg `0.3282` n `794`
- 24h: commodity avg `0.1769` n `12`; crypto_alt avg `1.5562` n `231`; crypto_major avg `2.1721` n `8`; equity avg `-1.4595` n `122`; fx avg `0.0173` n `6`; index avg `-0.2327` n `25`; metal avg `-0.0586` n `20`; unknown avg `0.5445` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
