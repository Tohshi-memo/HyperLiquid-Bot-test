# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T03:15:35.644751+00:00`
- Correlation status: `ready`
- Asset price records: `417`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.082` n `7`; crypto_alt avg `-0.1861` n `223`; crypto_major avg `-0.0791` n `7`; equity avg `0.0813` n `47`; fx avg `0.0128` n `4`; index avg `0.0132` n `6`; metal avg `0.2096` n `7`; unknown avg `-0.0081` n `313`
- 1h: commodity avg `0.1215` n `7`; crypto_alt avg `-0.0689` n `223`; crypto_major avg `-0.0193` n `7`; equity avg `0.1982` n `47`; fx avg `0.0151` n `4`; index avg `-0.0585` n `6`; metal avg `0.4604` n `7`; unknown avg `-0.0268` n `313`
- 4h: commodity avg `0.2516` n `7`; crypto_alt avg `0.8648` n `223`; crypto_major avg `0.0826` n `7`; equity avg `0.2465` n `47`; fx avg `-0.2693` n `4`; index avg `0.379` n `6`; metal avg `1.2382` n `7`; unknown avg `-0.1521` n `313`
- 24h: commodity avg `-1.3741` n `7`; crypto_alt avg `2.4732` n `223`; crypto_major avg `1.9088` n `7`; equity avg `2.6605` n `47`; fx avg `-0.1741` n `4`; index avg `2.1449` n `6`; metal avg `2.1244` n `7`; unknown avg `1.4762` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1832`, n `413`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.177`, n `413`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `413`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `413`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `413`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1061`, n `413`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1001`, n `409`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `413`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0961`, n `413`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0939`, n `409`, weak_sample_signal
