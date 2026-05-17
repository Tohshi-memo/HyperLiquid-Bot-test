# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T20:07:16.140551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0508` n `12`; crypto_alt avg `-0.0417` n `228`; crypto_major avg `0.0343` n `8`; equity avg `0.0399` n `65`; fx avg `0.0` n `5`; index avg `0.0323` n `23`; metal avg `-0.0039` n `18`; unknown avg `0.0201` n `384`
- 1h: commodity avg `-0.0775` n `12`; crypto_alt avg `0.1852` n `228`; crypto_major avg `0.4532` n `8`; equity avg `0.2274` n `65`; fx avg `0.0006` n `5`; index avg `0.0809` n `23`; metal avg `-0.0667` n `18`; unknown avg `0.1571` n `384`
- 4h: commodity avg `-0.013` n `12`; crypto_alt avg `0.0322` n `228`; crypto_major avg `1.1482` n `8`; equity avg `0.3226` n `65`; fx avg `0.011` n `5`; index avg `0.0731` n `23`; metal avg `-0.1315` n `18`; unknown avg `1.2439` n `384`
- 24h: commodity avg `1.7952` n `12`; crypto_alt avg `-9.1208` n `228`; crypto_major avg `-1.1812` n `8`; equity avg `-2.2544` n `65`; fx avg `-0.1549` n `5`; index avg `-1.5063` n `23`; metal avg `-5.9547` n `18`; unknown avg `551.2815` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0503`, n `668`, weak_sample_signal
