# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T11:37:28.564558+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0577` n `13`; crypto_alt avg `-0.0298` n `239`; crypto_major avg `-0.0618` n `8`; equity avg `0.0221` n `168`; fx avg `0.0052` n `6`; index avg `-0.0053` n `27`; metal avg `-0.0206` n `20`; unknown avg `0.0952` n `1267`
- 1h: commodity avg `0.2335` n `13`; crypto_alt avg `0.1277` n `239`; crypto_major avg `-0.0721` n `8`; equity avg `0.1538` n `168`; fx avg `-0.0242` n `6`; index avg `0.0184` n `27`; metal avg `0.0284` n `20`; unknown avg `0.5394` n `1263`
- 4h: commodity avg `0.2539` n `13`; crypto_alt avg `0.3829` n `239`; crypto_major avg `-0.1313` n `8`; equity avg `-0.0647` n `168`; fx avg `0.0067` n `6`; index avg `-0.0155` n `27`; metal avg `-0.0304` n `20`; unknown avg `176.1148` n `1149`
- 24h: commodity avg `0.5674` n `13`; crypto_alt avg `4.4252` n `239`; crypto_major avg `3.8213` n `8`; equity avg `4.1664` n `168`; fx avg `0.0917` n `6`; index avg `0.4139` n `27`; metal avg `0.838` n `20`; unknown avg `1.3369` n `1051`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
