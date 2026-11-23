# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T12:52:26.717395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0635` n `13`; crypto_alt avg `-0.1741` n `239`; crypto_major avg `-0.0958` n `8`; equity avg `-0.2425` n `166`; fx avg `-0.0349` n `6`; index avg `-0.0148` n `27`; metal avg `-0.1297` n `20`; unknown avg `0.0961` n `1262`
- 1h: commodity avg `-0.0304` n `13`; crypto_alt avg `-0.3913` n `239`; crypto_major avg `-0.3836` n `8`; equity avg `-0.9009` n `166`; fx avg `-0.0432` n `6`; index avg `-0.1352` n `27`; metal avg `-0.2` n `20`; unknown avg `0.4783` n `1252`
- 4h: commodity avg `-0.1797` n `13`; crypto_alt avg `-0.3461` n `239`; crypto_major avg `-0.2904` n `8`; equity avg `-0.6939` n `166`; fx avg `-0.1235` n `6`; index avg `-0.1064` n `27`; metal avg `-0.1506` n `20`; unknown avg `0.0318` n `1242`
- 24h: commodity avg `-0.919` n `13`; crypto_alt avg `0.4212` n `239`; crypto_major avg `1.0264` n `8`; equity avg `1.2253` n `166`; fx avg `0.1298` n `6`; index avg `-0.0066` n `27`; metal avg `0.209` n `20`; unknown avg `-0.2248` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
