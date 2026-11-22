# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T11:52:30.266107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1835` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0974` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0121` n `13`; crypto_alt avg `-0.0093` n `239`; crypto_major avg `-0.0027` n `8`; equity avg `-0.0159` n `166`; fx avg `0.0044` n `6`; index avg `-0.0014` n `27`; metal avg `0.0047` n `20`; unknown avg `-0.1184` n `1263`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `0.0776` n `239`; crypto_major avg `0.1636` n `8`; equity avg `0.0958` n `166`; fx avg `-0.0024` n `6`; index avg `-0.013` n `27`; metal avg `-0.0069` n `20`; unknown avg `158.8521` n `1257`
- 4h: commodity avg `0.0513` n `13`; crypto_alt avg `1.8053` n `239`; crypto_major avg `2.2348` n `8`; equity avg `1.1827` n `166`; fx avg `-0.026` n `6`; index avg `0.1014` n `27`; metal avg `0.1374` n `20`; unknown avg `89.7713` n `1141`
- 24h: commodity avg `0.0553` n `13`; crypto_alt avg `2.9157` n `239`; crypto_major avg `3.439` n `8`; equity avg `1.7697` n `166`; fx avg `-0.0116` n `6`; index avg `0.207` n `27`; metal avg `0.1618` n `20`; unknown avg `0.316` n `1086`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
