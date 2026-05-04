# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T12:30:31.822312+00:00`
- Correlation status: `ready`
- Asset price records: `265`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.092` n `7`; crypto_alt avg `0.1768` n `223`; crypto_major avg `0.1501` n `7`; equity avg `0.0259` n `42`; fx avg `0.0019` n `4`; index avg `0.1028` n `9`; metal avg `0.3281` n `7`; unknown avg `0.2768` n `314`
- 1h: commodity avg `-0.48` n `7`; crypto_alt avg `0.392` n `223`; crypto_major avg `0.2053` n `7`; equity avg `0.1138` n `42`; fx avg `0.0011` n `4`; index avg `0.1447` n `9`; metal avg `0.4796` n `7`; unknown avg `0.1636` n `314`
- 4h: commodity avg `-0.1799` n `7`; crypto_alt avg `-0.6259` n `223`; crypto_major avg `-0.9165` n `7`; equity avg `-0.3772` n `42`; fx avg `0.0004` n `4`; index avg `-0.2074` n `9`; metal avg `-0.2066` n `7`; unknown avg `-0.1886` n `314`
- 24h: commodity avg `0.5539` n `7`; crypto_alt avg `0.9513` n `223`; crypto_major avg `0.5176` n `7`; equity avg `0.3879` n `42`; fx avg `-0.0713` n `4`; index avg `0.5688` n `9`; metal avg `-1.2827` n `7`; unknown avg `-0.0208` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2763`, n `261`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2685`, n `261`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1804`, n `257`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.179`, n `261`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1702`, n `257`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1664`, n `261`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1664`, n `257`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.165`, n `257`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1627`, n `261`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.16`, n `257`, weak_sample_signal
