# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T20:07:30.400765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.0017` n `234`; crypto_major avg `0.0778` n `8`; equity avg `-0.1042` n `142`; fx avg `0.0065` n `6`; index avg `-0.0262` n `26`; metal avg `-0.0155` n `20`; unknown avg `86.5873` n `965`
- 1h: commodity avg `0.0632` n `13`; crypto_alt avg `-0.0131` n `234`; crypto_major avg `-0.0639` n `8`; equity avg `-0.0114` n `142`; fx avg `0.0172` n `6`; index avg `0.0155` n `26`; metal avg `0.056` n `20`; unknown avg `114.6159` n `965`
- 4h: commodity avg `0.1784` n `13`; crypto_alt avg `0.5353` n `234`; crypto_major avg `0.5025` n `8`; equity avg `0.8375` n `142`; fx avg `0.0004` n `6`; index avg `0.1982` n `26`; metal avg `0.1002` n `20`; unknown avg `1.0312` n `965`
- 24h: commodity avg `0.0309` n `13`; crypto_alt avg `0.3901` n `234`; crypto_major avg `0.5101` n `8`; equity avg `1.1485` n `142`; fx avg `-0.0879` n `6`; index avg `0.2362` n `26`; metal avg `0.0234` n `20`; unknown avg `1.0511` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
