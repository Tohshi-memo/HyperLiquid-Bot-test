# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T09:00:28.947400+00:00`
- Correlation status: `ready`
- Asset price records: `346`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0755` n `7`; crypto_alt avg `0.0012` n `223`; crypto_major avg `0.0403` n `7`; equity avg `-0.0462` n `47`; fx avg `0.04` n `4`; index avg `-0.1444` n `6`; metal avg `0.0449` n `7`; unknown avg `1.3694` n `312`
- 1h: commodity avg `-0.2052` n `7`; crypto_alt avg `-0.0699` n `223`; crypto_major avg `-0.1169` n `7`; equity avg `0.249` n `47`; fx avg `0.0418` n `4`; index avg `0.076` n `6`; metal avg `0.1603` n `7`; unknown avg `0.1283` n `312`
- 4h: commodity avg `-0.1461` n `7`; crypto_alt avg `0.5587` n `223`; crypto_major avg `0.2988` n `7`; equity avg `0.6027` n `47`; fx avg `0.0561` n `4`; index avg `0.2229` n `6`; metal avg `0.748` n `7`; unknown avg `1.7887` n `310`
- 24h: commodity avg `0.4184` n `7`; crypto_alt avg `1.1502` n `223`; crypto_major avg `0.67` n `7`; equity avg `0.0694` n `47`; fx avg `0.0207` n `4`; index avg `-0.0513` n `6`; metal avg `-0.0373` n `7`; unknown avg `1.2797` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2181`, n `342`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.211`, n `342`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `342`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1344`, n `342`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `342`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `342`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `342`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `342`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1046`, n `338`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0931`, n `338`, weak_sample_signal
