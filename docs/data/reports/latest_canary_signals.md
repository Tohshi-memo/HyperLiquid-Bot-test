# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T10:07:30.687951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5768` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0753` n `13`; crypto_alt avg `0.0001` n `239`; crypto_major avg `0.1379` n `8`; equity avg `0.1746` n `162`; fx avg `0.0001` n `6`; index avg `0.0165` n `27`; metal avg `0.0573` n `20`; unknown avg `0.063` n `1256`
- 1h: commodity avg `-0.1283` n `13`; crypto_alt avg `-0.0167` n `239`; crypto_major avg `0.4846` n `8`; equity avg `0.3093` n `162`; fx avg `-0.0205` n `6`; index avg `0.0297` n `27`; metal avg `0.0077` n `20`; unknown avg `158.7655` n `1260`
- 4h: commodity avg `-0.1065` n `13`; crypto_alt avg `1.4783` n `239`; crypto_major avg `1.5651` n `8`; equity avg `0.5902` n `162`; fx avg `-0.0003` n `6`; index avg `0.0542` n `27`; metal avg `-0.0117` n `20`; unknown avg `1.4598` n `1194`
- 24h: commodity avg `0.6424` n `13`; crypto_alt avg `-1.0849` n `239`; crypto_major avg `-2.9012` n `8`; equity avg `-1.3182` n `162`; fx avg `-0.032` n `6`; index avg `0.0048` n `27`; metal avg `-0.3846` n `20`; unknown avg `103.3458` n `1093`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
