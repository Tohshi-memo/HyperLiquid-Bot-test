# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T11:37:27.934521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `13`; crypto_alt avg `-0.0426` n `238`; crypto_major avg `0.0914` n `8`; equity avg `-0.0066` n `156`; fx avg `-0.0174` n `6`; index avg `-0.0004` n `27`; metal avg `-0.001` n `20`; unknown avg `198.8196` n `1258`
- 1h: commodity avg `0.0093` n `13`; crypto_alt avg `0.1147` n `238`; crypto_major avg `0.0538` n `8`; equity avg `-0.009` n `156`; fx avg `-0.0188` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0004` n `20`; unknown avg `204.4418` n `1224`
- 4h: commodity avg `0.0293` n `13`; crypto_alt avg `0.1948` n `238`; crypto_major avg `0.2032` n `8`; equity avg `-0.0577` n `156`; fx avg `-0.009` n `6`; index avg `-0.0126` n `27`; metal avg `0.0157` n `20`; unknown avg `207.357` n `1208`
- 24h: commodity avg `-0.233` n `13`; crypto_alt avg `0.2345` n `238`; crypto_major avg `-0.8057` n `8`; equity avg `-1.337` n `156`; fx avg `-0.0627` n `6`; index avg `-0.1375` n `27`; metal avg `-0.3506` n `20`; unknown avg `2.7936` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
