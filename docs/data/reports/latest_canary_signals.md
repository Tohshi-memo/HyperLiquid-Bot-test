# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T14:15:19.543406+00:00`
- Correlation status: `ready`
- Asset price records: `80`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `7`; crypto_alt avg `0.1913` n `223`; crypto_major avg `-0.1106` n `7`; equity avg `-0.0514` n `42`; fx avg `0.0104` n `4`; index avg `-0.001` n `9`; metal avg `0.001` n `7`; unknown avg `-0.0215` n `313`
- 1h: commodity avg `0.0093` n `7`; crypto_alt avg `0.42` n `223`; crypto_major avg `-0.026` n `7`; equity avg `-0.0039` n `42`; fx avg `-0.0035` n `4`; index avg `-0.0068` n `9`; metal avg `-0.0222` n `7`; unknown avg `0.074` n `313`
- 4h: commodity avg `-0.0333` n `7`; crypto_alt avg `0.5651` n `223`; crypto_major avg `-0.005` n `7`; equity avg `0.078` n `42`; fx avg `-0.017` n `4`; index avg `0.0841` n `9`; metal avg `-0.0109` n `7`; unknown avg `0.0048` n `313`
- 24h: commodity avg `0.9302` n `7`; crypto_alt avg `0.5513` n `223`; crypto_major avg `-0.3738` n `7`; equity avg `0.7102` n `42`; fx avg `-0.1358` n `4`; index avg `-0.3302` n `9`; metal avg `-1.1218` n `7`; unknown avg `0.9157` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5389`, n `76`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5203`, n `76`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5129`, n `72`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5029`, n `72`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4754`, n `72`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4732`, n `76`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.464`, n `72`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4639`, n `72`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4458`, n `76`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4275`, n `76`, moderate_sample_signal
