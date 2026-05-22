# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T06:22:18.060900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.0457` n `228`; crypto_major avg `0.1083` n `8`; equity avg `0.0458` n `67`; fx avg `0.0055` n `6`; index avg `0.0351` n `23`; metal avg `0.0452` n `18`; unknown avg `-0.2286` n `386`
- 1h: commodity avg `0.1825` n `12`; crypto_alt avg `-0.363` n `228`; crypto_major avg `-0.1801` n `8`; equity avg `-0.1361` n `67`; fx avg `0.0167` n `6`; index avg `0.0266` n `23`; metal avg `-0.1263` n `18`; unknown avg `-0.2664` n `376`
- 4h: commodity avg `0.1895` n `12`; crypto_alt avg `0.1318` n `228`; crypto_major avg `-0.2483` n `8`; equity avg `0.2559` n `67`; fx avg `0.0857` n `6`; index avg `0.1444` n `23`; metal avg `0.0964` n `18`; unknown avg `-0.3209` n `376`
- 24h: commodity avg `-0.496` n `12`; crypto_alt avg `1.789` n `228`; crypto_major avg `0.2644` n `8`; equity avg `1.3602` n `66`; fx avg `0.0979` n `6`; index avg `0.6946` n `23`; metal avg `0.484` n `18`; unknown avg `2.2516` n `375`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0493`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0414`, n `668`, weak_sample_signal
