# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T10:00:30.688900+00:00`
- Correlation status: `ready`
- Asset price records: `255`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `7`; crypto_alt avg `0.0181` n `223`; crypto_major avg `-0.0111` n `7`; equity avg `-0.0557` n `42`; fx avg `-0.0024` n `4`; index avg `-0.0204` n `9`; metal avg `-0.0692` n `7`; unknown avg `-0.0035` n `314`
- 1h: commodity avg `-0.0709` n `7`; crypto_alt avg `0.5478` n `223`; crypto_major avg `0.32` n `7`; equity avg `0.0008` n `42`; fx avg `0.0027` n `4`; index avg `-0.1243` n `9`; metal avg `-0.1117` n `7`; unknown avg `0.2079` n `314`
- 4h: commodity avg `0.5809` n `7`; crypto_alt avg `0.1908` n `223`; crypto_major avg `-0.3218` n `7`; equity avg `-0.2062` n `42`; fx avg `0.0087` n `4`; index avg `-0.327` n `9`; metal avg `-1.0397` n `7`; unknown avg `0.1649` n `314`
- 24h: commodity avg `0.5415` n `7`; crypto_alt avg `2.3508` n `223`; crypto_major avg `2.0459` n `7`; equity avg `0.9503` n `42`; fx avg `-0.0451` n `4`; index avg `0.5949` n `9`; metal avg `-1.1455` n `7`; unknown avg `0.3185` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3351`, n `251`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3244`, n `251`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.235`, n `247`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2328`, n `247`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2179`, n `247`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2053`, n `247`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1957`, n `251`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1811`, n `247`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `251`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.171`, n `251`, weak_sample_signal
