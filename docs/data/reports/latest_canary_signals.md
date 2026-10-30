# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T21:52:30.845058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `-0.2602` n `238`; crypto_major avg `-0.2567` n `8`; equity avg `-0.0533` n `156`; fx avg `-0.0169` n `6`; index avg `-0.0085` n `27`; metal avg `0.0138` n `20`; unknown avg `0.676` n `1261`
- 1h: commodity avg `0.0519` n `13`; crypto_alt avg `0.2703` n `238`; crypto_major avg `-0.1766` n `8`; equity avg `-0.0681` n `156`; fx avg `-0.0462` n `6`; index avg `0.014` n `27`; metal avg `0.0473` n `20`; unknown avg `0.7209` n `1239`
- 4h: commodity avg `-0.326` n `13`; crypto_alt avg `0.5751` n `238`; crypto_major avg `-0.1524` n `8`; equity avg `0.9883` n `156`; fx avg `-0.0192` n `6`; index avg `0.0811` n `27`; metal avg `0.0502` n `20`; unknown avg `1.5392` n `1149`
- 24h: commodity avg `0.1072` n `13`; crypto_alt avg `0.4252` n `238`; crypto_major avg `-1.5408` n `8`; equity avg `-3.1388` n `156`; fx avg `-0.1279` n `6`; index avg `-0.3036` n `27`; metal avg `-0.9646` n `20`; unknown avg `1.4067` n `1012`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1673`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
