# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T08:15:29.070135+00:00`
- Correlation status: `ready`
- Asset price records: `248`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0433` n `7`; crypto_alt avg `0.1307` n `223`; crypto_major avg `0.0507` n `7`; equity avg `-0.0981` n `42`; fx avg `-0.0011` n `4`; index avg `-0.1148` n `9`; metal avg `-0.0387` n `7`; unknown avg `-0.0163` n `314`
- 1h: commodity avg `0.3505` n `7`; crypto_alt avg `0.0639` n `223`; crypto_major avg `-0.0829` n `7`; equity avg `-0.1943` n `42`; fx avg `-0.0181` n `4`; index avg `-0.1412` n `9`; metal avg `-0.449` n `7`; unknown avg `0.4595` n `314`
- 4h: commodity avg `0.7457` n `7`; crypto_alt avg `-0.2789` n `223`; crypto_major avg `-0.7577` n `7`; equity avg `-0.4061` n `42`; fx avg `0.0293` n `4`; index avg `-0.0681` n `9`; metal avg `-1.2184` n `7`; unknown avg `-0.0152` n `312`
- 24h: commodity avg `0.8351` n `7`; crypto_alt avg `2.0817` n `223`; crypto_major avg `2.1698` n `7`; equity avg `0.954` n `42`; fx avg `-0.0661` n `4`; index avg `0.7331` n `9`; metal avg `-0.9486` n `7`; unknown avg `0.5692` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3435`, n `240`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3408`, n `244`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.337`, n `240`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3294`, n `244`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2061`, n `240`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1968`, n `240`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1842`, n `244`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1776`, n `244`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1716`, n `244`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1661`, n `240`, weak_sample_signal
