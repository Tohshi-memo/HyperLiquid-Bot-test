# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T03:52:28.802799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.016` n `230`; crypto_major avg `0.0599` n `8`; equity avg `0.021` n `114`; fx avg `0.0032` n `6`; index avg `0.0053` n `25`; metal avg `-0.0264` n `20`; unknown avg `2.0446` n `792`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `-0.0173` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `0.0832` n `114`; fx avg `-0.0012` n `6`; index avg `0.0205` n `25`; metal avg `-0.0196` n `20`; unknown avg `2.0905` n `792`
- 4h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.7696` n `230`; crypto_major avg `1.0712` n `8`; equity avg `0.5665` n `114`; fx avg `-0.0123` n `6`; index avg `0.0254` n `25`; metal avg `0.1885` n `20`; unknown avg `2.8789` n `792`
- 24h: commodity avg `-0.1265` n `12`; crypto_alt avg `0.2645` n `230`; crypto_major avg `0.6286` n `8`; equity avg `0.7206` n `114`; fx avg `-0.0176` n `6`; index avg `0.0784` n `25`; metal avg `0.1806` n `20`; unknown avg `2.2416` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
