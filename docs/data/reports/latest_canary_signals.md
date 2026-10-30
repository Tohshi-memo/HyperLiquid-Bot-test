# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T06:37:35.775592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8419` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0952` n `13`; crypto_alt avg `0.2493` n `238`; crypto_major avg `0.0384` n `8`; equity avg `0.1578` n `156`; fx avg `-0.0071` n `6`; index avg `0.0217` n `27`; metal avg `-0.014` n `20`; unknown avg `1.7673` n `1258`
- 1h: commodity avg `-0.0992` n `13`; crypto_alt avg `0.0026` n `238`; crypto_major avg `0.0074` n `8`; equity avg `-0.0035` n `156`; fx avg `-0.0139` n `6`; index avg `0.0237` n `27`; metal avg `-0.2178` n `20`; unknown avg `1.4465` n `1236`
- 4h: commodity avg `-0.1673` n `13`; crypto_alt avg `1.9906` n `238`; crypto_major avg `1.6719` n `8`; equity avg `0.512` n `156`; fx avg `-0.0786` n `6`; index avg `0.083` n `27`; metal avg `-0.17` n `20`; unknown avg `1.6013` n `1214`
- 24h: commodity avg `-0.1996` n `13`; crypto_alt avg `-3.125` n `238`; crypto_major avg `0.3263` n `8`; equity avg `-2.6344` n `155`; fx avg `0.1113` n `6`; index avg `-0.3352` n `27`; metal avg `-0.6376` n `20`; unknown avg `31.173` n `980`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
