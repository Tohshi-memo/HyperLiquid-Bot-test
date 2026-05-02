# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T05:45:17.607185+00:00`
- Correlation status: `ready`
- Asset price records: `46`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `7`; crypto_alt avg `0.1111` n `223`; crypto_major avg `0.0042` n `7`; equity avg `0.0943` n `42`; fx avg `-0.033` n `4`; index avg `0.0135` n `9`; metal avg `-0.001` n `7`; unknown avg `-0.0371` n `311`
- 1h: commodity avg `-0.0068` n `7`; crypto_alt avg `-0.0847` n `223`; crypto_major avg `-0.1284` n `7`; equity avg `0.0829` n `42`; fx avg `-0.1054` n `4`; index avg `0.0121` n `9`; metal avg `0.0007` n `7`; unknown avg `-0.0208` n `311`
- 4h: commodity avg `-0.0142` n `7`; crypto_alt avg `-0.4873` n `223`; crypto_major avg `-0.2129` n `7`; equity avg `0.1092` n `42`; fx avg `-0.1555` n `4`; index avg `-0.0006` n `9`; metal avg `-0.0282` n `7`; unknown avg `-0.0308` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6565`, n `42`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6335`, n `42`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5959`, n `38`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5804`, n `38`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5479`, n `42`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.543`, n `38`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5302`, n `38`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5235`, n `38`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5107`, n `42`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5066`, n `42`, strong_sample_signal
