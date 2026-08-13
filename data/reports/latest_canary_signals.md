# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T10:37:45.568191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0502` n `12`; crypto_alt avg `-0.0211` n `230`; crypto_major avg `-0.1318` n `8`; equity avg `-0.1284` n `113`; fx avg `0.005` n `6`; index avg `-0.0096` n `25`; metal avg `0.0133` n `20`; unknown avg `0.0494` n `787`
- 1h: commodity avg `-0.0232` n `12`; crypto_alt avg `0.0518` n `230`; crypto_major avg `-0.1034` n `8`; equity avg `0.0148` n `113`; fx avg `0.0183` n `6`; index avg `0.014` n `25`; metal avg `0.0842` n `20`; unknown avg `0.0468` n `787`
- 4h: commodity avg `-0.3481` n `12`; crypto_alt avg `0.0254` n `230`; crypto_major avg `-0.3188` n `8`; equity avg `-0.4231` n `113`; fx avg `0.0316` n `6`; index avg `-0.0251` n `25`; metal avg `0.0469` n `20`; unknown avg `0.0512` n `787`
- 24h: commodity avg `-0.3348` n `12`; crypto_alt avg `-0.5502` n `230`; crypto_major avg `-0.522` n `8`; equity avg `1.1873` n `113`; fx avg `0.0451` n `6`; index avg `0.1385` n `25`; metal avg `-0.5023` n `20`; unknown avg `0.1472` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2307`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1831`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
