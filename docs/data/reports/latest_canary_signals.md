# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T14:52:29.497802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `0.0048` n `239`; crypto_major avg `0.2123` n `8`; equity avg `0.0318` n `166`; fx avg `0.0127` n `6`; index avg `-0.0042` n `27`; metal avg `0.0349` n `20`; unknown avg `158.1993` n `1263`
- 1h: commodity avg `-0.0103` n `13`; crypto_alt avg `-0.0748` n `239`; crypto_major avg `0.2483` n `8`; equity avg `0.0657` n `166`; fx avg `0.0042` n `6`; index avg `-0.0072` n `27`; metal avg `0.0442` n `20`; unknown avg `159.7887` n `1251`
- 4h: commodity avg `-0.038` n `13`; crypto_alt avg `-0.1015` n `239`; crypto_major avg `-0.0095` n `8`; equity avg `0.0671` n `166`; fx avg `0.0128` n `6`; index avg `0.0312` n `27`; metal avg `0.01` n `20`; unknown avg `160.3922` n `1245`
- 24h: commodity avg `-0.0363` n `13`; crypto_alt avg `0.3397` n `239`; crypto_major avg `0.578` n `8`; equity avg `0.9666` n `166`; fx avg `-0.0087` n `6`; index avg `0.161` n `27`; metal avg `0.0313` n `20`; unknown avg `-0.2203` n `1076`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
