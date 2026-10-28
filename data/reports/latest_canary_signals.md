# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T12:07:28.333914+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.47` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0563` n `13`; crypto_alt avg `-0.4207` n `238`; crypto_major avg `-0.3797` n `8`; equity avg `-0.2279` n `154`; fx avg `0.0337` n `6`; index avg `-0.0229` n `27`; metal avg `0.0017` n `20`; unknown avg `0.1356` n `1227`
- 1h: commodity avg `-0.0816` n `13`; crypto_alt avg `-0.2765` n `238`; crypto_major avg `-0.3278` n `8`; equity avg `-0.2251` n `154`; fx avg `0.0682` n `6`; index avg `0.0023` n `27`; metal avg `0.056` n `20`; unknown avg `0.0757` n `1227`
- 4h: commodity avg `0.0735` n `13`; crypto_alt avg `0.018` n `238`; crypto_major avg `0.0315` n `8`; equity avg `-0.1477` n `154`; fx avg `0.0834` n `6`; index avg `-0.0136` n `27`; metal avg `-0.0254` n `20`; unknown avg `88.273` n `1196`
- 24h: commodity avg `0.0531` n `13`; crypto_alt avg `2.2416` n `238`; crypto_major avg `2.2312` n `8`; equity avg `2.9618` n `154`; fx avg `0.1309` n `6`; index avg `0.4032` n `27`; metal avg `0.3023` n `20`; unknown avg `7.1594` n `1068`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
