# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T09:22:25.774045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.1` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0702` n `12`; crypto_alt avg `-0.3223` n `228`; crypto_major avg `-0.1352` n `8`; equity avg `-0.0467` n `72`; fx avg `-0.0234` n `6`; index avg `0.0311` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.0908` n `420`
- 1h: commodity avg `0.1014` n `12`; crypto_alt avg `-0.2741` n `228`; crypto_major avg `-0.0424` n `8`; equity avg `-0.1452` n `72`; fx avg `-0.0004` n `6`; index avg `0.0018` n `23`; metal avg `0.168` n `18`; unknown avg `-0.0917` n `420`
- 4h: commodity avg `0.9123` n `12`; crypto_alt avg `0.1962` n `228`; crypto_major avg `-0.0819` n `8`; equity avg `-0.2403` n `72`; fx avg `0.0245` n `6`; index avg `-0.0595` n `23`; metal avg `-0.4974` n `18`; unknown avg `0.7439` n `410`
- 24h: commodity avg `2.0777` n `12`; crypto_alt avg `-0.9445` n `228`; crypto_major avg `-3.1262` n `8`; equity avg `0.5455` n `72`; fx avg `0.0395` n `6`; index avg `0.8959` n `23`; metal avg `-1.5265` n `18`; unknown avg `0.8077` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
