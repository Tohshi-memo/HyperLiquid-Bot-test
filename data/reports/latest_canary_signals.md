# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T10:44:15.886916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `-0.0301` n `230`; crypto_major avg `0.0146` n `8`; equity avg `-0.1884` n `102`; fx avg `-0.0004` n `6`; index avg `-0.0487` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0011` n `774`
- 1h: commodity avg `0.0964` n `12`; crypto_alt avg `-0.0503` n `230`; crypto_major avg `-0.1782` n `8`; equity avg `-0.4188` n `102`; fx avg `-0.0452` n `6`; index avg `-0.0806` n `25`; metal avg `-0.1198` n `20`; unknown avg `-0.0132` n `774`
- 4h: commodity avg `-0.0269` n `12`; crypto_alt avg `-0.1795` n `230`; crypto_major avg `-0.2527` n `8`; equity avg `-0.2126` n `102`; fx avg `-0.0506` n `6`; index avg `-0.0615` n `25`; metal avg `-0.2177` n `20`; unknown avg `-0.0172` n `774`
- 24h: commodity avg `-0.4226` n `12`; crypto_alt avg `-3.6343` n `230`; crypto_major avg `-3.8176` n `8`; equity avg `-4.5543` n `102`; fx avg `-0.1862` n `6`; index avg `-0.9582` n `25`; metal avg `-0.7153` n `20`; unknown avg `998.1215` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
