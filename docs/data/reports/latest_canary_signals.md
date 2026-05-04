# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T22:29:53.879713+00:00`
- Correlation status: `ready`
- Asset price records: `303`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0839` n `7`; crypto_alt avg `-0.2022` n `223`; crypto_major avg `-0.1686` n `7`; equity avg `0.0057` n `47`; fx avg `-0.0001` n `4`; index avg `-0.0486` n `6`; metal avg `0.0116` n `7`; unknown avg `-0.0305` n `312`
- 1h: commodity avg `-0.0872` n `7`; crypto_alt avg `0.3017` n `223`; crypto_major avg `0.2345` n `7`; equity avg `0.1906` n `47`; fx avg `0.0007` n `4`; index avg `-0.1393` n `6`; metal avg `-0.0315` n `7`; unknown avg `0.1338` n `312`
- 4h: commodity avg `-0.1285` n `7`; crypto_alt avg `0.0288` n `223`; crypto_major avg `-0.1206` n `7`; equity avg `-0.0955` n `47`; fx avg `-0.0006` n `4`; index avg `-0.1695` n `6`; metal avg `-0.0188` n `7`; unknown avg `-0.3448` n `312`
- 24h: commodity avg `1.6147` n `7`; crypto_alt avg `1.7087` n `223`; crypto_major avg `0.7235` n `7`; equity avg `-0.2517` n `47`; fx avg `-0.022` n `4`; index avg `-0.1997` n `6`; metal avg `-2.2754` n `7`; unknown avg `-1.2891` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2357`, n `299`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2298`, n `299`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1683`, n `295`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1671`, n `295`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1498`, n `299`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `299`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.141`, n `299`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `299`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `295`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1197`, n `299`, weak_sample_signal
