# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T10:22:28.037491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.0794` n `234`; crypto_major avg `0.0383` n `8`; equity avg `0.0012` n `140`; fx avg `0.0052` n `6`; index avg `-0.0011` n `26`; metal avg `-0.014` n `20`; unknown avg `0.4452` n `943`
- 1h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.6002` n `234`; crypto_major avg `-0.1998` n `8`; equity avg `-0.0233` n `140`; fx avg `-0.0008` n `6`; index avg `0.0132` n `26`; metal avg `-0.0225` n `20`; unknown avg `0.0574` n `941`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `-0.9878` n `234`; crypto_major avg `-0.2704` n `8`; equity avg `-0.0552` n `140`; fx avg `0.0071` n `6`; index avg `-0.0055` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.3906` n `935`
- 24h: commodity avg `0.2473` n `12`; crypto_alt avg `-2.0668` n `234`; crypto_major avg `-2.1502` n `8`; equity avg `-0.3048` n `140`; fx avg `-0.0736` n `6`; index avg `-0.0616` n `26`; metal avg `0.0026` n `20`; unknown avg `0.5089` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
