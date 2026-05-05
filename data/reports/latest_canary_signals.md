# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T00:00:29.502134+00:00`
- Correlation status: `ready`
- Asset price records: `310`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0333` n `7`; crypto_alt avg `0.168` n `223`; crypto_major avg `0.0206` n `7`; equity avg `-0.038` n `47`; fx avg `0.0` n `4`; index avg `-0.0054` n `6`; metal avg `0.0507` n `7`; unknown avg `0.0317` n `312`
- 1h: commodity avg `0.0048` n `7`; crypto_alt avg `-0.125` n `223`; crypto_major avg `-0.2858` n `7`; equity avg `-0.0323` n `47`; fx avg `-0.0018` n `4`; index avg `0.0043` n `6`; metal avg `0.0763` n `7`; unknown avg `0.0193` n `312`
- 4h: commodity avg `-0.069` n `7`; crypto_alt avg `-0.0544` n `223`; crypto_major avg `-0.1619` n `7`; equity avg `-0.1839` n `47`; fx avg `0.0132` n `4`; index avg `-0.2445` n `6`; metal avg `-0.0334` n `7`; unknown avg `-0.1198` n `312`
- 24h: commodity avg `1.2861` n `7`; crypto_alt avg `1.9449` n `223`; crypto_major avg `0.9366` n `7`; equity avg `-0.5024` n `47`; fx avg `-0.0239` n `4`; index avg `-0.1244` n `6`; metal avg `-2.3423` n `7`; unknown avg `-1.1621` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2358`, n `306`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.23`, n `306`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1894`, n `302`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1874`, n `302`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1499`, n `306`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1474`, n `306`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `306`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1301`, n `306`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `302`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1203`, n `306`, weak_sample_signal
