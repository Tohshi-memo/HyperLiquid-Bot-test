# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T12:45:20.133917+00:00`
- Correlation status: `ready`
- Asset price records: `266`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1905` n `7`; crypto_alt avg `-0.1343` n `223`; crypto_major avg `0.0057` n `7`; equity avg `0.0029` n `42`; fx avg `0.0059` n `4`; index avg `-0.0424` n `9`; metal avg `0.03` n `7`; unknown avg `0.004` n `314`
- 1h: commodity avg `-0.6281` n `7`; crypto_alt avg `0.1703` n `223`; crypto_major avg `0.2416` n `7`; equity avg `0.1749` n `42`; fx avg `0.0041` n `4`; index avg `0.121` n `9`; metal avg `0.6183` n `7`; unknown avg `0.1949` n `314`
- 4h: commodity avg `-0.2871` n `7`; crypto_alt avg `-0.6667` n `223`; crypto_major avg `-0.9273` n `7`; equity avg `-0.3783` n `42`; fx avg `-0.0059` n `4`; index avg `-0.1988` n `9`; metal avg `-0.2301` n `7`; unknown avg `-0.1837` n `314`
- 24h: commodity avg `0.3674` n `7`; crypto_alt avg `0.8149` n `223`; crypto_major avg `0.5239` n `7`; equity avg `0.3936` n `42`; fx avg `-0.0654` n `4`; index avg `0.4825` n `9`; metal avg `-1.2543` n `7`; unknown avg `0.0101` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2704`, n `262`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2624`, n `262`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.179`, n `258`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1718`, n `262`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1694`, n `258`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `262`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1613`, n `262`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1608`, n `258`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1597`, n `258`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1587`, n `258`, weak_sample_signal
