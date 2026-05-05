# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T09:15:27.463364+00:00`
- Correlation status: `ready`
- Asset price records: `347`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1484` n `7`; crypto_alt avg `0.0002` n `223`; crypto_major avg `-0.0278` n `7`; equity avg `-0.0143` n `47`; fx avg `0.023` n `4`; index avg `0.0263` n `6`; metal avg `0.0382` n `7`; unknown avg `-0.0072` n `312`
- 1h: commodity avg `-0.0211` n `7`; crypto_alt avg `-0.288` n `223`; crypto_major avg `-0.2172` n `7`; equity avg `-0.0038` n `47`; fx avg `0.0378` n `4`; index avg `-0.0782` n `6`; metal avg `0.1045` n `7`; unknown avg `-0.298` n `312`
- 4h: commodity avg `-0.0885` n `7`; crypto_alt avg `0.1911` n `223`; crypto_major avg `0.1397` n `7`; equity avg `0.4036` n `47`; fx avg `0.0577` n `4`; index avg `0.1674` n `6`; metal avg `0.567` n `7`; unknown avg `0.5291` n `310`
- 24h: commodity avg `0.663` n `7`; crypto_alt avg `0.9634` n `223`; crypto_major avg `0.4646` n `7`; equity avg `-0.0593` n `47`; fx avg `0.0268` n `4`; index avg `0.0571` n `6`; metal avg `-0.1032` n `7`; unknown avg `-0.9945` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2178`, n `343`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2107`, n `343`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.139`, n `343`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `343`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1175`, n `343`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `343`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `343`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `343`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `339`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `339`, weak_sample_signal
