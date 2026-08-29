# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T10:18:41.099456+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.1882` n `231`; crypto_major avg `0.2517` n `8`; equity avg `0.022` n `127`; fx avg `-0.0014` n `6`; index avg `0.0025` n `26`; metal avg `0.0007` n `20`; unknown avg `0.0449` n `793`
- 1h: commodity avg `0.0101` n `12`; crypto_alt avg `0.1808` n `231`; crypto_major avg `0.1771` n `8`; equity avg `0.0258` n `127`; fx avg `-0.0169` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.0426` n `791`
- 4h: commodity avg `0.0515` n `12`; crypto_alt avg `0.012` n `231`; crypto_major avg `0.3627` n `8`; equity avg `0.0726` n `127`; fx avg `-0.0117` n `6`; index avg `-0.0101` n `26`; metal avg `0.0125` n `20`; unknown avg `0.0788` n `791`
- 24h: commodity avg `-0.0568` n `12`; crypto_alt avg `-1.718` n `231`; crypto_major avg `-1.6046` n `8`; equity avg `-1.3203` n `127`; fx avg `-0.0319` n `6`; index avg `-0.1349` n `26`; metal avg `-0.6956` n `20`; unknown avg `-0.3623` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
