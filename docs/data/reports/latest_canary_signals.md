# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T14:52:29.571856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2953` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0861` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6575` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.013` n `13`; crypto_alt avg `-0.2838` n `239`; crypto_major avg `-0.4598` n `8`; equity avg `0.3602` n `162`; fx avg `-0.0078` n `6`; index avg `0.0243` n `27`; metal avg `-0.0864` n `20`; unknown avg `0.8002` n `1261`
- 1h: commodity avg `-0.0612` n `13`; crypto_alt avg `-0.1006` n `239`; crypto_major avg `-0.4479` n `8`; equity avg `0.704` n `162`; fx avg `-0.0114` n `6`; index avg `0.0912` n `27`; metal avg `-0.0322` n `20`; unknown avg `2.4498` n `1255`
- 4h: commodity avg `0.2252` n `13`; crypto_alt avg `-1.3777` n `239`; crypto_major avg `-2.0701` n `8`; equity avg `-0.8561` n `162`; fx avg `-0.0175` n `6`; index avg `0.016` n `27`; metal avg `-0.4126` n `20`; unknown avg `23.3321` n `1247`
- 24h: commodity avg `-0.1142` n `13`; crypto_alt avg `-3.2941` n `239`; crypto_major avg `-2.8992` n `8`; equity avg `-1.4454` n `162`; fx avg `-0.0721` n `6`; index avg `-0.0005` n `27`; metal avg `-0.9812` n `20`; unknown avg `2.5679` n `1146`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
