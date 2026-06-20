# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T14:07:31.905578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2337` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1302` n `12`; crypto_alt avg `-0.631` n `228`; crypto_major avg `-0.5083` n `8`; equity avg `-0.1433` n `78`; fx avg `0.0037` n `6`; index avg `-0.0154` n `23`; metal avg `-0.0064` n `18`; unknown avg `-0.1731` n `701`
- 1h: commodity avg `0.3004` n `12`; crypto_alt avg `-1.0185` n `228`; crypto_major avg `-1.0128` n `8`; equity avg `-0.4067` n `78`; fx avg `-0.0174` n `6`; index avg `-0.0406` n `23`; metal avg `-0.0609` n `18`; unknown avg `-0.0075` n `701`
- 4h: commodity avg `0.2685` n `12`; crypto_alt avg `-1.5423` n `228`; crypto_major avg `-1.2772` n `8`; equity avg `-0.4458` n `78`; fx avg `0.0038` n `6`; index avg `-0.0435` n `23`; metal avg `-0.0388` n `18`; unknown avg `-0.4524` n `573`
- 24h: commodity avg `0.8` n `12`; crypto_alt avg `-4.2351` n `228`; crypto_major avg `-4.409` n `8`; equity avg `0.7809` n `78`; fx avg `-0.085` n `6`; index avg `0.2623` n `23`; metal avg `-4.1455` n `18`; unknown avg `-0.48` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
