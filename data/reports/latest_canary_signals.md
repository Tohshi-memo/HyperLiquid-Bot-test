# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T12:03:48.801670+00:00`
- Correlation status: `ready`
- Asset price records: `263`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1785` n `7`; crypto_alt avg `0.1066` n `223`; crypto_major avg `0.0523` n `7`; equity avg `0.1532` n `42`; fx avg `-0.0091` n `4`; index avg `0.0244` n `9`; metal avg `0.1178` n `7`; unknown avg `-0.0519` n `314`
- 1h: commodity avg `-0.2174` n `7`; crypto_alt avg `0.0837` n `223`; crypto_major avg `-0.1004` n `7`; equity avg `0.2645` n `42`; fx avg `-0.0107` n `4`; index avg `0.0747` n `9`; metal avg `-0.2267` n `7`; unknown avg `-0.2522` n `314`
- 4h: commodity avg `-0.0471` n `7`; crypto_alt avg `-0.8196` n `223`; crypto_major avg `-1.1918` n `7`; equity avg `-0.5417` n `42`; fx avg `-0.006` n `4`; index avg `-0.4198` n `9`; metal avg `-0.7525` n `7`; unknown avg `-0.5338` n `314`
- 24h: commodity avg `0.8139` n `7`; crypto_alt avg `0.9944` n `223`; crypto_major avg `0.4721` n `7`; equity avg `0.4034` n `42`; fx avg `-0.0754` n `4`; index avg `0.4267` n `9`; metal avg `-1.7284` n `7`; unknown avg `-0.3349` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2803`, n `259`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2726`, n `259`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1842`, n `259`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1811`, n `255`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1729`, n `255`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1712`, n `259`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1711`, n `255`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1707`, n `255`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.163`, n `259`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1606`, n `255`, weak_sample_signal
