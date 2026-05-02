# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T23:15:32.778731+00:00`
- Correlation status: `ready`
- Asset price records: `116`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `7`; crypto_alt avg `-0.0101` n `223`; crypto_major avg `0.006` n `7`; equity avg `-0.0031` n `42`; fx avg `0.0024` n `4`; index avg `0.0004` n `9`; metal avg `0.0074` n `7`; unknown avg `0.0152` n `313`
- 1h: commodity avg `0.0673` n `7`; crypto_alt avg `-0.0699` n `223`; crypto_major avg `0.0003` n `7`; equity avg `-0.0017` n `42`; fx avg `-0.0077` n `4`; index avg `-0.0154` n `9`; metal avg `0.0115` n `7`; unknown avg `-0.0721` n `313`
- 4h: commodity avg `0.0423` n `7`; crypto_alt avg `0.0653` n `223`; crypto_major avg `-0.085` n `7`; equity avg `0.2724` n `42`; fx avg `0.0377` n `4`; index avg `-0.0195` n `9`; metal avg `0.02` n `7`; unknown avg `0.0787` n `313`
- 24h: commodity avg `-0.1688` n `7`; crypto_alt avg `2.0583` n `223`; crypto_major avg `0.6862` n `7`; equity avg `0.7162` n `42`; fx avg `0.0144` n `4`; index avg `-0.0244` n `9`; metal avg `0.041` n `7`; unknown avg `0.3201` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4863`, n `112`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4695`, n `112`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4637`, n `108`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4164`, n `108`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4143`, n `108`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4136`, n `108`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4092`, n `108`, moderate_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4088`, n `108`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `112`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3852`, n `112`, moderate_sample_signal
