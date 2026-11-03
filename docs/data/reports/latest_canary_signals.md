# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T10:01:11.448009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `13`; crypto_alt avg `0.0097` n `239`; crypto_major avg `0.0162` n `8`; equity avg `0.0735` n `157`; fx avg `-0.0117` n `6`; index avg `0.0043` n `27`; metal avg `0.0043` n `20`; unknown avg `-0.0105` n `1256`
- 1h: commodity avg `-0.152` n `13`; crypto_alt avg `0.1906` n `239`; crypto_major avg `0.1604` n `8`; equity avg `0.3178` n `157`; fx avg `-0.0006` n `6`; index avg `0.0314` n `27`; metal avg `0.0927` n `20`; unknown avg `0.6127` n `1256`
- 4h: commodity avg `0.1997` n `13`; crypto_alt avg `0.426` n `239`; crypto_major avg `0.6827` n `8`; equity avg `1.1388` n `157`; fx avg `0.0699` n `6`; index avg `0.1067` n `27`; metal avg `-0.1623` n `20`; unknown avg `20.0304` n `1224`
- 24h: commodity avg `-0.4065` n `13`; crypto_alt avg `-1.6364` n `238`; crypto_major avg `-0.9259` n `8`; equity avg `-3.5309` n `157`; fx avg `-0.0039` n `6`; index avg `-0.2276` n `27`; metal avg `-0.4404` n `20`; unknown avg `4.425` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
