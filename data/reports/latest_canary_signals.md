# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T16:52:25.563384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0129` n `13`; crypto_alt avg `-0.0439` n `239`; crypto_major avg `-0.0366` n `8`; equity avg `0.0664` n `166`; fx avg `0.003` n `6`; index avg `0.0091` n `27`; metal avg `0.0042` n `20`; unknown avg `158.1781` n `1263`
- 1h: commodity avg `0.0361` n `13`; crypto_alt avg `0.1573` n `239`; crypto_major avg `0.298` n `8`; equity avg `0.0764` n `166`; fx avg `0.0107` n `6`; index avg `0.015` n `27`; metal avg `0.0223` n `20`; unknown avg `164.6873` n `1245`
- 4h: commodity avg `-0.0174` n `13`; crypto_alt avg `0.0851` n `239`; crypto_major avg `0.5303` n `8`; equity avg `0.109` n `166`; fx avg `0.0167` n `6`; index avg `0.0429` n `27`; metal avg `0.0598` n `20`; unknown avg `2.193` n `1239`
- 24h: commodity avg `0.0005` n `13`; crypto_alt avg `1.0991` n `239`; crypto_major avg `1.313` n `8`; equity avg `0.9806` n `166`; fx avg `0.0166` n `6`; index avg `0.1775` n `27`; metal avg `0.0859` n `20`; unknown avg `3.0733` n `1072`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
