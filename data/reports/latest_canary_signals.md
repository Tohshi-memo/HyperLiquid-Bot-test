# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T09:52:29.333923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2742` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1934` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `0.5469` n `239`; crypto_major avg `0.7699` n `8`; equity avg `0.215` n `166`; fx avg `0.0006` n `6`; index avg `0.0183` n `27`; metal avg `0.0364` n `20`; unknown avg `2.5769` n `1219`
- 1h: commodity avg `0.038` n `13`; crypto_alt avg `0.664` n `239`; crypto_major avg `1.1406` n `8`; equity avg `0.2745` n `166`; fx avg `0.0035` n `6`; index avg `0.0217` n `27`; metal avg `0.0753` n `20`; unknown avg `2.9148` n `1213`
- 4h: commodity avg `0.0512` n `13`; crypto_alt avg `1.5619` n `239`; crypto_major avg `2.3254` n `8`; equity avg `0.8471` n `166`; fx avg `-0.0251` n `6`; index avg `0.0878` n `27`; metal avg `0.132` n `20`; unknown avg `3.381` n `1175`
- 24h: commodity avg `0.0736` n `13`; crypto_alt avg `2.6346` n `239`; crypto_major avg `4.0189` n `8`; equity avg `1.5545` n `166`; fx avg `0.0348` n `6`; index avg `0.1792` n `27`; metal avg `0.1584` n `20`; unknown avg `425.3221` n `1070`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
