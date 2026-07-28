# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T17:37:33.442162+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0597` n `12`; crypto_alt avg `-0.4009` n `230`; crypto_major avg `-0.5182` n `8`; equity avg `-0.1467` n `102`; fx avg `-0.0078` n `6`; index avg `0.0078` n `25`; metal avg `-0.043` n `20`; unknown avg `0.0623` n `774`
- 1h: commodity avg `0.2842` n `12`; crypto_alt avg `-0.5712` n `230`; crypto_major avg `-0.5412` n `8`; equity avg `0.0126` n `102`; fx avg `-0.0028` n `6`; index avg `-0.0469` n `25`; metal avg `-0.1003` n `20`; unknown avg `0.1348` n `774`
- 4h: commodity avg `-0.4703` n `12`; crypto_alt avg `0.3684` n `230`; crypto_major avg `0.8788` n `8`; equity avg `0.6296` n `102`; fx avg `-0.0343` n `6`; index avg `0.1322` n `25`; metal avg `0.2132` n `20`; unknown avg `-0.1237` n `774`
- 24h: commodity avg `-0.9661` n `12`; crypto_alt avg `-2.4273` n `230`; crypto_major avg `-2.4127` n `8`; equity avg `-2.5687` n `102`; fx avg `-0.0695` n `6`; index avg `-0.1904` n `25`; metal avg `-0.3378` n `20`; unknown avg `17.8113` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
