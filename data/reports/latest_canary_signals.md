# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T17:37:28.361687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `13`; crypto_alt avg `0.1525` n `238`; crypto_major avg `0.1187` n `8`; equity avg `0.0126` n `156`; fx avg `0.0001` n `6`; index avg `0.0014` n `27`; metal avg `-0.0` n `20`; unknown avg `-0.2028` n `1263`
- 1h: commodity avg `0.008` n `13`; crypto_alt avg `0.1175` n `238`; crypto_major avg `0.1537` n `8`; equity avg `0.01` n `156`; fx avg `-0.0147` n `6`; index avg `0.0007` n `27`; metal avg `0.0104` n `20`; unknown avg `159.3258` n `1257`
- 4h: commodity avg `-0.0389` n `13`; crypto_alt avg `-0.4447` n `238`; crypto_major avg `0.0736` n `8`; equity avg `0.0172` n `156`; fx avg `0.0173` n `6`; index avg `0.0502` n `27`; metal avg `0.0016` n `20`; unknown avg `0.1531` n `1245`
- 24h: commodity avg `0.0214` n `13`; crypto_alt avg `-0.3119` n `238`; crypto_major avg `0.2463` n `8`; equity avg `0.486` n `156`; fx avg `-0.0051` n `6`; index avg `0.099` n `27`; metal avg `0.0516` n `20`; unknown avg `4.2163` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
