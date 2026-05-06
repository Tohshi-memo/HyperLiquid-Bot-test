# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T12:07:18.425558+00:00`
- Correlation status: `ready`
- Asset price records: `452`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.787` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.6277` n `7`; crypto_alt avg `-0.1298` n `223`; crypto_major avg `-0.1957` n `7`; equity avg `-0.2962` n `47`; fx avg `0.0185` n `4`; index avg `-0.204` n `6`; metal avg `-0.3` n `7`; unknown avg `-0.1632` n `313`
- 1h: commodity avg `1.2625` n `7`; crypto_alt avg `-0.3787` n `223`; crypto_major avg `-0.0119` n `7`; equity avg `-0.4448` n `47`; fx avg `0.1029` n `4`; index avg `0.0147` n `6`; metal avg `-0.6637` n `7`; unknown avg `-0.4043` n `313`
- 4h: commodity avg `-1.4645` n `7`; crypto_alt avg `0.9944` n `223`; crypto_major avg `1.3225` n `7`; equity avg `0.7897` n `47`; fx avg `-0.0302` n `4`; index avg `1.2328` n `6`; metal avg `0.4066` n `7`; unknown avg `0.1114` n `313`
- 24h: commodity avg `-3.2265` n `7`; crypto_alt avg `3.4721` n `223`; crypto_major avg `2.8004` n `7`; equity avg `3.1066` n `47`; fx avg `-0.5963` n `4`; index avg `3.0839` n `6`; metal avg `2.1463` n `7`; unknown avg `1.826` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1661`, n `448`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1601`, n `448`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1476`, n `448`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `448`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `448`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.116`, n `448`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `444`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1049`, n `444`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0984`, n `444`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `444`, weak_sample_signal
