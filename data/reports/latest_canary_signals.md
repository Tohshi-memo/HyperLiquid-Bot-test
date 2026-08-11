# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T16:37:28.459913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.0597` n `230`; crypto_major avg `-0.0314` n `8`; equity avg `-0.0229` n `113`; fx avg `-0.0142` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0136` n `20`; unknown avg `-0.0427` n `785`
- 1h: commodity avg `-0.0707` n `12`; crypto_alt avg `0.2836` n `230`; crypto_major avg `0.3055` n `8`; equity avg `-0.1094` n `113`; fx avg `-0.017` n `6`; index avg `-0.0057` n `25`; metal avg `0.0591` n `20`; unknown avg `0.0769` n `785`
- 4h: commodity avg `0.0028` n `12`; crypto_alt avg `-1.1905` n `230`; crypto_major avg `-0.7349` n `8`; equity avg `0.0287` n `113`; fx avg `-0.0115` n `6`; index avg `-0.0692` n `25`; metal avg `-0.0605` n `20`; unknown avg `0.1406` n `785`
- 24h: commodity avg `0.1695` n `12`; crypto_alt avg `-1.9584` n `230`; crypto_major avg `-0.2034` n `8`; equity avg `0.1334` n `113`; fx avg `-0.0658` n `6`; index avg `0.0918` n `25`; metal avg `0.0404` n `20`; unknown avg `-0.2781` n `753`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.214`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1997`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
