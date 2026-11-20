# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T20:22:27.374998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0724` n `13`; crypto_alt avg `0.2578` n `239`; crypto_major avg `0.333` n `8`; equity avg `0.3257` n `166`; fx avg `0.0103` n `6`; index avg `0.0184` n `27`; metal avg `0.084` n `20`; unknown avg `2.2575` n `1260`
- 1h: commodity avg `0.0986` n `13`; crypto_alt avg `0.0451` n `239`; crypto_major avg `0.5137` n `8`; equity avg `-0.5888` n `166`; fx avg `-0.0096` n `6`; index avg `-0.0799` n `27`; metal avg `0.0215` n `20`; unknown avg `16.7764` n `1248`
- 4h: commodity avg `0.5425` n `13`; crypto_alt avg `-0.6045` n `239`; crypto_major avg `-1.2437` n `8`; equity avg `-2.3337` n `166`; fx avg `-0.0138` n `6`; index avg `-0.3394` n `27`; metal avg `-0.1905` n `20`; unknown avg `409.5093` n `1249`
- 24h: commodity avg `0.2045` n `13`; crypto_alt avg `-5.9961` n `239`; crypto_major avg `-6.6224` n `8`; equity avg `-8.2975` n `166`; fx avg `0.0075` n `6`; index avg `-0.8111` n `27`; metal avg `-1.2117` n `20`; unknown avg `51.8034` n `1155`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
