# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T05:30:38.575108+00:00`
- Correlation status: `ready`
- Asset price records: `45`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `7`; crypto_alt avg `0.0333` n `223`; crypto_major avg `0.081` n `7`; equity avg `0.0122` n `42`; fx avg `-0.0584` n `4`; index avg `0.0006` n `9`; metal avg `0.0084` n `7`; unknown avg `0.0247` n `311`
- 1h: commodity avg `-0.0066` n `7`; crypto_alt avg `-0.2475` n `223`; crypto_major avg `-0.1401` n `7`; equity avg `-0.0153` n `42`; fx avg `-0.0775` n `4`; index avg `-0.0064` n `9`; metal avg `-0.0018` n `7`; unknown avg `0.0495` n `311`
- 4h: commodity avg `0.0001` n `7`; crypto_alt avg `-0.6544` n `223`; crypto_major avg `-0.2076` n `7`; equity avg `-0.0841` n `42`; fx avg `-0.1248` n `4`; index avg `-0.0443` n `9`; metal avg `-0.0201` n `7`; unknown avg `0.0102` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.656`, n `41`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6329`, n `41`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.6032`, n `37`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5805`, n `37`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5556`, n `37`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5442`, n `41`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5374`, n `37`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5306`, n `37`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5113`, n `41`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5023`, n `41`, strong_sample_signal
