# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T15:22:28.919167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.7318` n `234`; crypto_major avg `-0.6185` n `8`; equity avg `0.0661` n `140`; fx avg `-0.0022` n `6`; index avg `0.0129` n `26`; metal avg `0.0062` n `20`; unknown avg `0.0037` n `942`
- 1h: commodity avg `0.0284` n `12`; crypto_alt avg `0.1375` n `234`; crypto_major avg `0.4717` n `8`; equity avg `0.4072` n `140`; fx avg `0.0208` n `6`; index avg `0.0846` n `26`; metal avg `-0.032` n `20`; unknown avg `0.2486` n `904`
- 4h: commodity avg `-0.1975` n `12`; crypto_alt avg `-0.3295` n `234`; crypto_major avg `0.5261` n `8`; equity avg `0.7946` n `140`; fx avg `0.0071` n `6`; index avg `0.1789` n `26`; metal avg `0.0029` n `20`; unknown avg `11.637` n `856`
- 24h: commodity avg `-0.958` n `12`; crypto_alt avg `6.4152` n `234`; crypto_major avg `6.1087` n `8`; equity avg `2.7251` n `140`; fx avg `-0.0506` n `6`; index avg `0.5438` n `26`; metal avg `0.0434` n `20`; unknown avg `4.2629` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
