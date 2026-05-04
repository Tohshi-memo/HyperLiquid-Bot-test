# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T10:30:30.286284+00:00`
- Correlation status: `ready`
- Asset price records: `257`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7982` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.3574` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `1.105` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1205` n `7`; crypto_alt avg `-0.0551` n `223`; crypto_major avg `-0.0631` n `7`; equity avg `0.1276` n `42`; fx avg `-0.0015` n `4`; index avg `0.1004` n `9`; metal avg `0.3249` n `7`; unknown avg `-0.0012` n `314`
- 1h: commodity avg `0.8945` n `7`; crypto_alt avg `-1.3042` n `223`; crypto_major avg `-1.4629` n `7`; equity avg `-1.1449` n `42`; fx avg `-0.0278` n `4`; index avg `-0.3579` n `9`; metal avg `-0.9913` n `7`; unknown avg `-0.3555` n `314`
- 4h: commodity avg `1.4211` n `7`; crypto_alt avg `-1.0632` n `223`; crypto_major avg `-1.3771` n `7`; equity avg `-1.1787` n `42`; fx avg `-0.023` n `4`; index avg `-0.6836` n `9`; metal avg `-1.7566` n `7`; unknown avg `-0.1778` n `314`
- 24h: commodity avg `1.5138` n `7`; crypto_alt avg `0.5543` n `223`; crypto_major avg `0.3806` n `7`; equity avg `-0.1198` n `42`; fx avg `-0.07` n `4`; index avg `0.2151` n `9`; metal avg `-1.9265` n `7`; unknown avg `-0.231` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2932`, n `253`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2851`, n `253`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2053`, n `249`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2052`, n `249`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2027`, n `249`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.195`, n `253`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1853`, n `249`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.183`, n `249`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1809`, n `253`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `253`, weak_sample_signal
