# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T07:37:26.521329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `13`; crypto_alt avg `-0.0191` n `239`; crypto_major avg `-0.1583` n `8`; equity avg `0.0308` n `166`; fx avg `0.0172` n `6`; index avg `0.0061` n `27`; metal avg `-0.0599` n `20`; unknown avg `11.2921` n `1266`
- 1h: commodity avg `-0.0948` n `13`; crypto_alt avg `0.0822` n `239`; crypto_major avg `0.05` n `8`; equity avg `0.2226` n `166`; fx avg `-0.0055` n `6`; index avg `0.0259` n `27`; metal avg `0.085` n `20`; unknown avg `8.9802` n `1264`
- 4h: commodity avg `-0.2161` n `13`; crypto_alt avg `0.4252` n `239`; crypto_major avg `-0.1689` n `8`; equity avg `0.2534` n `166`; fx avg `0.0252` n `6`; index avg `-0.0535` n `27`; metal avg `0.1731` n `20`; unknown avg `5.3863` n `1228`
- 24h: commodity avg `-0.5528` n `13`; crypto_alt avg `2.5871` n `239`; crypto_major avg `2.9829` n `8`; equity avg `2.6395` n `166`; fx avg `0.2294` n `6`; index avg `0.1734` n `27`; metal avg `0.6027` n `20`; unknown avg `342.9109` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
