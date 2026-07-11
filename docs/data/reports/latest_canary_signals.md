# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T21:37:26.438241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.125` n `230`; crypto_major avg `-0.0288` n `8`; equity avg `-0.0165` n `92`; fx avg `0.0043` n `6`; index avg `0.0011` n `25`; metal avg `0.0019` n `20`; unknown avg `0.0385` n `765`
- 1h: commodity avg `-0.0365` n `12`; crypto_alt avg `-0.1836` n `230`; crypto_major avg `0.0356` n `8`; equity avg `-0.0063` n `92`; fx avg `0.0049` n `6`; index avg `-0.006` n `25`; metal avg `-0.0107` n `20`; unknown avg `-0.0166` n `765`
- 4h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.0198` n `230`; crypto_major avg `0.146` n `8`; equity avg `0.0821` n `92`; fx avg `0.0` n `6`; index avg `-0.0112` n `25`; metal avg `-0.0096` n `20`; unknown avg `-0.2652` n `765`
- 24h: commodity avg `0.0146` n `12`; crypto_alt avg `0.755` n `229`; crypto_major avg `0.8172` n `8`; equity avg `0.3543` n `92`; fx avg `0.0095` n `6`; index avg `0.0116` n `25`; metal avg `-0.0258` n `20`; unknown avg `2.7124` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
