# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T17:07:27.552950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0288` n `12`; crypto_alt avg `-0.0161` n `228`; crypto_major avg `-0.1928` n `8`; equity avg `-0.2552` n `74`; fx avg `-0.0003` n `6`; index avg `-0.1082` n `23`; metal avg `-0.078` n `18`; unknown avg `-0.0443` n `517`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.2953` n `228`; crypto_major avg `-0.626` n `8`; equity avg `-0.1434` n `74`; fx avg `-0.0009` n `6`; index avg `-0.0774` n `23`; metal avg `-0.0108` n `18`; unknown avg `-0.0794` n `517`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.1422` n `228`; crypto_major avg `-0.0478` n `8`; equity avg `0.1165` n `74`; fx avg `0.0012` n `6`; index avg `-0.0747` n `23`; metal avg `0.0822` n `18`; unknown avg `-0.3173` n `517`
- 24h: commodity avg `-0.5602` n `12`; crypto_alt avg `1.6988` n `228`; crypto_major avg `2.5837` n `8`; equity avg `2.104` n `74`; fx avg `-0.2538` n `6`; index avg `0.9768` n `23`; metal avg `0.0767` n `18`; unknown avg `-2.0924` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
