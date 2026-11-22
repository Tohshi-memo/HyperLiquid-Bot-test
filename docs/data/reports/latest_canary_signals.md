# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T11:57:43.286951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1817` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0876` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0049` n `13`; crypto_alt avg `-0.0216` n `239`; crypto_major avg `-0.012` n `8`; equity avg `0.0102` n `166`; fx avg `0.0137` n `6`; index avg `0.0017` n `27`; metal avg `0.0054` n `20`; unknown avg `0.0306` n `1261`
- 1h: commodity avg `0.0017` n `13`; crypto_alt avg `0.0652` n `239`; crypto_major avg `0.1544` n `8`; equity avg `0.1219` n `166`; fx avg `0.0069` n `6`; index avg `-0.0098` n `27`; metal avg `-0.0062` n `20`; unknown avg `159.1143` n `1255`
- 4h: commodity avg `0.044` n `13`; crypto_alt avg `1.7924` n `239`; crypto_major avg `2.2257` n `8`; equity avg `1.2095` n `166`; fx avg `-0.0167` n `6`; index avg `0.1046` n `27`; metal avg `0.1381` n `20`; unknown avg `46.3425` n `1135`
- 24h: commodity avg `0.048` n `13`; crypto_alt avg `2.9027` n `239`; crypto_major avg `3.4298` n `8`; equity avg `1.7966` n `166`; fx avg `-0.0023` n `6`; index avg `0.2102` n `27`; metal avg `0.1625` n `20`; unknown avg `0.3324` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
