# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T12:07:40.077139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2101` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.038` n `228`; crypto_major avg `0.0685` n `8`; equity avg `-0.0563` n `86`; fx avg `-0.002` n `6`; index avg `0.008` n `23`; metal avg `0.0083` n `20`; unknown avg `0.048` n `765`
- 1h: commodity avg `0.0718` n `12`; crypto_alt avg `-0.0196` n `228`; crypto_major avg `0.1305` n `8`; equity avg `-0.1457` n `86`; fx avg `-0.0157` n `6`; index avg `-0.0268` n `23`; metal avg `0.0336` n `20`; unknown avg `0.1274` n `765`
- 4h: commodity avg `-0.0614` n `12`; crypto_alt avg `-0.9754` n `228`; crypto_major avg `-1.2093` n `8`; equity avg `-0.1647` n `86`; fx avg `-0.0227` n `6`; index avg `0.0008` n `23`; metal avg `0.066` n `20`; unknown avg `-0.0117` n `765`
- 24h: commodity avg `-0.1153` n `12`; crypto_alt avg `-2.1232` n `228`; crypto_major avg `-1.9895` n `8`; equity avg `-0.0504` n `86`; fx avg `-0.0236` n `6`; index avg `0.4549` n `23`; metal avg `-0.6307` n `20`; unknown avg `-0.6074` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
