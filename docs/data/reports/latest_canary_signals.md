# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T10:52:32.417148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2001` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0877` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.0193` n `239`; crypto_major avg `0.0042` n `8`; equity avg `0.0331` n `166`; fx avg `-0.0039` n `6`; index avg `0.0049` n `27`; metal avg `0.0201` n `20`; unknown avg `158.3817` n `1263`
- 1h: commodity avg `-0.0051` n `13`; crypto_alt avg `0.3352` n `239`; crypto_major avg `0.0838` n `8`; equity avg `0.2243` n `166`; fx avg `-0.0131` n `6`; index avg `0.0361` n `27`; metal avg `0.0278` n `20`; unknown avg `141.4074` n `1203`
- 4h: commodity avg `0.0462` n `13`; crypto_alt avg `1.815` n `239`; crypto_major avg `2.2463` n `8`; equity avg `1.0509` n `166`; fx avg `-0.034` n `6`; index avg `0.1195` n `27`; metal avg `0.1586` n `20`; unknown avg `150.5885` n `1139`
- 24h: commodity avg `0.0778` n `13`; crypto_alt avg `3.145` n `239`; crypto_major avg `3.8576` n `8`; equity avg `1.8317` n `166`; fx avg `0.0064` n `6`; index avg `0.2275` n `27`; metal avg `0.1659` n `20`; unknown avg `0.1746` n `1054`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
