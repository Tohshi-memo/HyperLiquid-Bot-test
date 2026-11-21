# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T23:29:19.157296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `13`; crypto_alt avg `0.0988` n `239`; crypto_major avg `0.1229` n `8`; equity avg `0.0414` n `166`; fx avg `-0.005` n `6`; index avg `0.019` n `27`; metal avg `-0.0067` n `20`; unknown avg `2.7734` n `1252`
- 1h: commodity avg `0.0163` n `13`; crypto_alt avg `0.0995` n `239`; crypto_major avg `-0.0279` n `8`; equity avg `-0.0664` n `166`; fx avg `0.0083` n `6`; index avg `0.0125` n `27`; metal avg `-0.0009` n `20`; unknown avg `165.0791` n `1242`
- 4h: commodity avg `0.024` n `13`; crypto_alt avg `0.0657` n `239`; crypto_major avg `-0.1229` n `8`; equity avg `0.1449` n `166`; fx avg `0.0131` n `6`; index avg `0.0724` n `27`; metal avg `-0.0728` n `20`; unknown avg `209.6118` n `1198`
- 24h: commodity avg `0.023` n `13`; crypto_alt avg `-0.0791` n `239`; crypto_major avg `1.5214` n `8`; equity avg `0.2605` n `166`; fx avg `-0.0309` n `6`; index avg `0.1282` n `27`; metal avg `0.084` n `20`; unknown avg `601.7203` n `1082`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
