# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T17:22:25.182221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2251` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.0791` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7846` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0269` n `13`; crypto_alt avg `-0.0015` n `239`; crypto_major avg `0.178` n `8`; equity avg `-0.2984` n `162`; fx avg `0.0187` n `6`; index avg `-0.042` n `27`; metal avg `0.001` n `20`; unknown avg `6.5671` n `1261`
- 1h: commodity avg `-0.1408` n `13`; crypto_alt avg `0.4609` n `239`; crypto_major avg `0.641` n `8`; equity avg `-0.552` n `162`; fx avg `0.0189` n `6`; index avg `-0.0799` n `27`; metal avg `0.0853` n `20`; unknown avg `0.9494` n `1261`
- 4h: commodity avg `-0.4177` n `13`; crypto_alt avg `1.6735` n `239`; crypto_major avg `1.6614` n `8`; equity avg `-0.5637` n `162`; fx avg `-0.0123` n `6`; index avg `-0.0241` n `27`; metal avg `-0.1232` n `20`; unknown avg `3.161` n `1229`
- 24h: commodity avg `-0.9139` n `13`; crypto_alt avg `0.6578` n `239`; crypto_major avg `0.7098` n `8`; equity avg `-2.3026` n `162`; fx avg `-0.0283` n `6`; index avg `-0.1718` n `27`; metal avg `-0.109` n `20`; unknown avg `231.0348` n `1037`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
