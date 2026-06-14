# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T14:52:33.899126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2357` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.2198` n `12`; crypto_alt avg `-0.065` n `228`; crypto_major avg `-0.1024` n `8`; equity avg `0.0406` n `74`; fx avg `0.0045` n `6`; index avg `-0.0466` n `23`; metal avg `0.025` n `18`; unknown avg `0.2512` n `645`
- 1h: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.7562` n `228`; crypto_major avg `-0.7451` n `8`; equity avg `-0.2412` n `74`; fx avg `-0.008` n `6`; index avg `-0.0661` n `23`; metal avg `-0.0372` n `18`; unknown avg `0.0161` n `645`
- 4h: commodity avg `0.3004` n `12`; crypto_alt avg `-1.4526` n `228`; crypto_major avg `-1.2364` n `8`; equity avg `-0.4524` n `74`; fx avg `0.0083` n `6`; index avg `-0.0007` n `23`; metal avg `-0.1426` n `18`; unknown avg `-0.1041` n `645`
- 24h: commodity avg `-0.0771` n `12`; crypto_alt avg `-1.6425` n `228`; crypto_major avg `-1.1858` n `8`; equity avg `0.2524` n `74`; fx avg `0.0056` n `6`; index avg `0.063` n `23`; metal avg `-0.0322` n `18`; unknown avg `-1.2858` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
