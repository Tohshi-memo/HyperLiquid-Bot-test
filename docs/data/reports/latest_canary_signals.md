# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T13:22:29.008550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `13`; crypto_alt avg `0.0618` n `234`; crypto_major avg `-0.0065` n `8`; equity avg `-0.0068` n `142`; fx avg `-0.0018` n `6`; index avg `-0.0216` n `26`; metal avg `-0.0074` n `20`; unknown avg `2.2847` n `975`
- 1h: commodity avg `-0.0282` n `13`; crypto_alt avg `-0.6345` n `234`; crypto_major avg `-0.648` n `8`; equity avg `-0.1721` n `142`; fx avg `-0.0297` n `6`; index avg `-0.0533` n `26`; metal avg `-0.0914` n `20`; unknown avg `2.4856` n `973`
- 4h: commodity avg `-0.1406` n `13`; crypto_alt avg `-1.0054` n `234`; crypto_major avg `-0.3205` n `8`; equity avg `-0.2612` n `142`; fx avg `-0.0342` n `6`; index avg `-0.0086` n `26`; metal avg `0.1847` n `20`; unknown avg `2.7217` n `967`
- 24h: commodity avg `-0.3392` n `13`; crypto_alt avg `-2.7526` n `234`; crypto_major avg `-1.7689` n `8`; equity avg `-0.3137` n `142`; fx avg `0.0417` n `6`; index avg `0.0464` n `26`; metal avg `-0.1309` n `20`; unknown avg `780.219` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
