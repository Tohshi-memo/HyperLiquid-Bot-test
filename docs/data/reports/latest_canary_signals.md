# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T11:30:27.601592+00:00`
- Correlation status: `ready`
- Asset price records: `261`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `7`; crypto_alt avg `-0.1859` n `223`; crypto_major avg `-0.1265` n `7`; equity avg `-0.0024` n `42`; fx avg `0.0011` n `4`; index avg `-0.0153` n `9`; metal avg `-0.1548` n `7`; unknown avg `-0.1443` n `314`
- 1h: commodity avg `-0.4689` n `7`; crypto_alt avg `0.2076` n `223`; crypto_major avg `0.3423` n `7`; equity avg `0.5666` n `42`; fx avg `0.0042` n `4`; index avg `0.1999` n `9`; metal avg `0.2243` n `7`; unknown avg `0.1617` n `314`
- 4h: commodity avg `0.52` n `7`; crypto_alt avg `-1.0916` n `223`; crypto_major avg `-1.3309` n `7`; equity avg `-0.7214` n `42`; fx avg `-0.0116` n `4`; index avg `-0.4358` n `9`; metal avg `-1.1974` n `7`; unknown avg `0.06` n `314`
- 24h: commodity avg `1.063` n `7`; crypto_alt avg `0.9574` n `223`; crypto_major avg `0.755` n `7`; equity avg `0.3323` n `42`; fx avg `-0.0769` n `4`; index avg `0.392` n `9`; metal avg `-1.7302` n `7`; unknown avg `0.065` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2804`, n `257`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2725`, n `257`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1872`, n `253`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1853`, n `253`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1832`, n `253`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.183`, n `257`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1717`, n `253`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.171`, n `257`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1632`, n `253`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1626`, n `257`, weak_sample_signal
