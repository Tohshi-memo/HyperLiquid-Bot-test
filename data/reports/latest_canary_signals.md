# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T17:07:33.237804+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `13`; crypto_alt avg `-0.0601` n `239`; crypto_major avg `-0.1991` n `8`; equity avg `0.0347` n `166`; fx avg `-0.003` n `6`; index avg `-0.0017` n `27`; metal avg `-0.0069` n `20`; unknown avg `0.3894` n `1245`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `-0.0004` n `239`; crypto_major avg `0.0613` n `8`; equity avg `0.1243` n `166`; fx avg `0.0005` n `6`; index avg `0.0126` n `27`; metal avg `-0.004` n `20`; unknown avg `-0.2285` n `1251`
- 4h: commodity avg `-0.0306` n `13`; crypto_alt avg `0.0963` n `239`; crypto_major avg `0.4546` n `8`; equity avg `0.1122` n `166`; fx avg `0.0142` n `6`; index avg `0.0358` n `27`; metal avg `0.0618` n `20`; unknown avg `325.0572` n `1229`
- 24h: commodity avg `-0.03` n `13`; crypto_alt avg `0.9513` n `239`; crypto_major avg `1.0224` n `8`; equity avg `0.9632` n `166`; fx avg `0.0016` n `6`; index avg `0.1681` n `27`; metal avg `0.0615` n `20`; unknown avg `0.0147` n `1062`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
