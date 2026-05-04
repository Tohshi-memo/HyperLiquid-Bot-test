# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T10:15:20.359223+00:00`
- Correlation status: `ready`
- Asset price records: `256`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.3899` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.6298` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `1.0544` n `7`; crypto_alt avg `-1.6981` n `223`; crypto_major avg `-1.6693` n `7`; equity avg `-1.1506` n `42`; fx avg `-0.0193` n `4`; index avg `-0.4451` n `9`; metal avg `-1.1021` n `7`; unknown avg `-0.563` n `314`
- 1h: commodity avg `1.1403` n `7`; crypto_alt avg `-1.3046` n `223`; crypto_major avg `-1.4895` n `7`; equity avg `-1.278` n `42`; fx avg `-0.0132` n `4`; index avg `-0.514` n `9`; metal avg `-1.3392` n `7`; unknown avg `-0.5462` n `314`
- 4h: commodity avg `1.6701` n `7`; crypto_alt avg `-1.2794` n `223`; crypto_major avg `-1.7198` n `7`; equity avg `-1.3357` n `42`; fx avg `-0.0219` n `4`; index avg `-0.7701` n `9`; metal avg `-2.0252` n `7`; unknown avg `-0.2879` n `314`
- 24h: commodity avg `1.6083` n `7`; crypto_alt avg `0.5819` n `223`; crypto_major avg `0.4395` n `7`; equity avg `-0.1911` n `42`; fx avg `-0.0645` n `4`; index avg `0.1409` n `9`; metal avg `-2.2336` n `7`; unknown avg `-0.2557` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3053`, n `252`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2963`, n `252`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2061`, n `248`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1927`, n `252`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1895`, n `248`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1811`, n `248`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1811`, n `248`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1795`, n `248`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1754`, n `248`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1748`, n `248`, weak_sample_signal
