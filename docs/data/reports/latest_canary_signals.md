# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T13:37:29.881933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `0.0078` n `230`; crypto_major avg `-0.0026` n `8`; equity avg `0.0106` n `100`; fx avg `-0.001` n `6`; index avg `0.0032` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0003` n `774`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.2902` n `230`; crypto_major avg `0.2503` n `8`; equity avg `-0.0177` n `100`; fx avg `0.0049` n `6`; index avg `0.0034` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0036` n `774`
- 4h: commodity avg `-0.0937` n `12`; crypto_alt avg `0.3065` n `230`; crypto_major avg `0.3225` n `8`; equity avg `0.0524` n `100`; fx avg `-0.0088` n `6`; index avg `-0.0032` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.0562` n `774`
- 24h: commodity avg `-0.2788` n `12`; crypto_alt avg `-0.0915` n `230`; crypto_major avg `0.06` n `8`; equity avg `-1.9972` n `100`; fx avg `-0.0025` n `6`; index avg `-0.1443` n `25`; metal avg `-0.0127` n `20`; unknown avg `13.2772` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1244`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1079`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
