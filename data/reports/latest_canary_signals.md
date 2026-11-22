# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T00:37:24.558422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `13`; crypto_alt avg `-0.031` n `239`; crypto_major avg `-0.0497` n `8`; equity avg `0.0283` n `166`; fx avg `0.0076` n `6`; index avg `0.0021` n `27`; metal avg `-0.0044` n `20`; unknown avg `0.0523` n `1263`
- 1h: commodity avg `0.0043` n `13`; crypto_alt avg `0.0023` n `239`; crypto_major avg `0.0401` n `8`; equity avg `0.1276` n `166`; fx avg `-0.0032` n `6`; index avg `0.0011` n `27`; metal avg `0.0013` n `20`; unknown avg `175.3819` n `1256`
- 4h: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.0718` n `239`; crypto_major avg `-0.1958` n `8`; equity avg `0.09` n `166`; fx avg `0.0044` n `6`; index avg `0.0477` n `27`; metal avg `-0.0516` n `20`; unknown avg `-0.119` n `1214`
- 24h: commodity avg `0.049` n `13`; crypto_alt avg `0.3385` n `239`; crypto_major avg `1.7307` n `8`; equity avg `0.6488` n `166`; fx avg `-0.0343` n `6`; index avg `0.1757` n `27`; metal avg `0.0908` n `20`; unknown avg `233.3023` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
