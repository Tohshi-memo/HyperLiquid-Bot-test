# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T02:26:04.914821+00:00`
- Correlation status: `ready`
- Asset price records: `509`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0378` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1597` n `12`; crypto_alt avg `-0.1195` n `228`; crypto_major avg `-0.1145` n `8`; equity avg `-0.1119` n `65`; fx avg `0.0084` n `4`; index avg `-0.0251` n `23`; metal avg `-0.3274` n `18`; unknown avg `-0.1373` n `358`
- 1h: commodity avg `-0.1242` n `12`; crypto_alt avg `-0.0633` n `228`; crypto_major avg `-0.2372` n `8`; equity avg `0.1776` n `65`; fx avg `0.0018` n `4`; index avg `0.0711` n `23`; metal avg `-0.2542` n `18`; unknown avg `-0.2511` n `357`
- 4h: commodity avg `-0.1163` n `12`; crypto_alt avg `-1.0702` n `228`; crypto_major avg `-0.9181` n `8`; equity avg `0.0494` n `65`; fx avg `0.0802` n `4`; index avg `0.1197` n `23`; metal avg `0.1434` n `18`; unknown avg `-0.6987` n `356`
- 24h: commodity avg `-1.7629` n `7`; crypto_alt avg `-0.0323` n `223`; crypto_major avg `-1.1433` n `7`; equity avg `1.5863` n `47`; fx avg `-0.2616` n `4`; index avg `1.0953` n `6`; metal avg `2.0239` n `7`; unknown avg `2.2388` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `505`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `505`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `505`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.078`, n `501`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `505`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0707`, n `501`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `501`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `501`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `505`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0647`, n `501`, weak_sample_signal
