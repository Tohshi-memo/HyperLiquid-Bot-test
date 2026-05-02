# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T17:30:23.143786+00:00`
- Correlation status: `ready`
- Asset price records: `93`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `7`; crypto_alt avg `-0.0309` n `223`; crypto_major avg `0.0046` n `7`; equity avg `0.0536` n `42`; fx avg `-0.0011` n `4`; index avg `0.0` n `9`; metal avg `-0.0004` n `7`; unknown avg `-0.0082` n `313`
- 1h: commodity avg `-0.0519` n `7`; crypto_alt avg `0.1473` n `223`; crypto_major avg `0.005` n `7`; equity avg `0.0082` n `42`; fx avg `0.0349` n `4`; index avg `0.0047` n `9`; metal avg `0.0082` n `7`; unknown avg `0.092` n `313`
- 4h: commodity avg `-0.072` n `7`; crypto_alt avg `1.2191` n `223`; crypto_major avg `0.2015` n `7`; equity avg `0.0244` n `42`; fx avg `0.0912` n `4`; index avg `-0.002` n `9`; metal avg `-0.0117` n `7`; unknown avg `0.1026` n `313`
- 24h: commodity avg `0.3123` n `7`; crypto_alt avg `1.563` n `223`; crypto_major avg `0.3801` n `7`; equity avg `0.6359` n `42`; fx avg `-0.0447` n `4`; index avg `0.1348` n `9`; metal avg `-0.4573` n `7`; unknown avg `0.8708` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5268`, n `89`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5202`, n `85`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5084`, n `89`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4919`, n `85`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4692`, n `85`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4564`, n `85`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4539`, n `85`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4522`, n `89`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4253`, n `89`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4208`, n `85`, moderate_sample_signal
