# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T15:56:07.899420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.7427` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.6193` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `0.163` n `239`; crypto_major avg `0.06` n `8`; equity avg `-0.378` n `168`; fx avg `-0.018` n `6`; index avg `-0.0572` n `27`; metal avg `-0.095` n `20`; unknown avg `4.0413` n `1264`
- 1h: commodity avg `0.0692` n `13`; crypto_alt avg `1.0821` n `239`; crypto_major avg `1.5337` n `8`; equity avg `0.4715` n `168`; fx avg `0.0144` n `6`; index avg `0.0488` n `27`; metal avg `-0.0856` n `20`; unknown avg `43.1673` n `1257`
- 4h: commodity avg `0.4884` n `13`; crypto_alt avg `-0.3708` n `239`; crypto_major avg `-0.1691` n `8`; equity avg `-1.9118` n `168`; fx avg `0.0333` n `6`; index avg `-0.1786` n `27`; metal avg `-0.5514` n `20`; unknown avg `423.686` n `1239`
- 24h: commodity avg `0.7663` n `13`; crypto_alt avg `-1.2265` n `239`; crypto_major avg `-2.0744` n `8`; equity avg `-4.6994` n `168`; fx avg `-0.0442` n `6`; index avg `-0.4718` n `27`; metal avg `-1.1802` n `20`; unknown avg `633.5857` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
