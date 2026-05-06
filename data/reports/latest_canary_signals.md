# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T05:15:27.743352+00:00`
- Correlation status: `ready`
- Asset price records: `425`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.246` n `7`; crypto_alt avg `-0.1113` n `223`; crypto_major avg `-0.046` n `7`; equity avg `0.0076` n `47`; fx avg `0.0409` n `4`; index avg `-0.0021` n `6`; metal avg `0.0226` n `7`; unknown avg `0.057` n `313`
- 1h: commodity avg `0.1994` n `7`; crypto_alt avg `-0.5559` n `223`; crypto_major avg `-0.4161` n `7`; equity avg `0.0059` n `47`; fx avg `-0.2063` n `4`; index avg `0.0632` n `6`; metal avg `-0.002` n `7`; unknown avg `0.3974` n `313`
- 4h: commodity avg `0.018` n `7`; crypto_alt avg `0.2787` n `223`; crypto_major avg `0.1455` n `7`; equity avg `0.687` n `47`; fx avg `-0.1885` n `4`; index avg `0.1376` n `6`; metal avg `0.9507` n `7`; unknown avg `0.0814` n `313`
- 24h: commodity avg `-1.2772` n `7`; crypto_alt avg `2.0338` n `223`; crypto_major avg `1.5809` n `7`; equity avg `2.8769` n `47`; fx avg `-0.3806` n `4`; index avg `2.2397` n `6`; metal avg `2.1858` n `7`; unknown avg `1.4035` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1809`, n `421`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1746`, n `421`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `421`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `421`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `421`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `421`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1014`, n `417`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0962`, n `417`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `421`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `421`, weak_sample_signal
