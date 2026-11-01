# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T09:22:26.754270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `13`; crypto_alt avg `-0.1726` n `238`; crypto_major avg `-0.2078` n `8`; equity avg `0.003` n `156`; fx avg `-0.0015` n `6`; index avg `0.0016` n `27`; metal avg `-0.0007` n `20`; unknown avg `0.0722` n `1263`
- 1h: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.0229` n `238`; crypto_major avg `0.2463` n `8`; equity avg `0.1696` n `156`; fx avg `-0.0067` n `6`; index avg `0.0148` n `27`; metal avg `0.0049` n `20`; unknown avg `-0.0424` n `1257`
- 4h: commodity avg `-0.0014` n `13`; crypto_alt avg `0.0574` n `238`; crypto_major avg `0.1728` n `8`; equity avg `0.2384` n `156`; fx avg `-0.0095` n `6`; index avg `0.0331` n `27`; metal avg `0.0164` n `20`; unknown avg `1.0437` n `1224`
- 24h: commodity avg `-0.0338` n `13`; crypto_alt avg `0.6708` n `238`; crypto_major avg `0.677` n `8`; equity avg `0.5006` n `156`; fx avg `-0.0115` n `6`; index avg `0.036` n `27`; metal avg `0.0641` n `20`; unknown avg `2.6568` n `996`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
