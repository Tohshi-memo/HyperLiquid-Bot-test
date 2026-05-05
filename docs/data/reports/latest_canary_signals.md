# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T12:15:29.257194+00:00`
- Correlation status: `ready`
- Asset price records: `359`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0862` n `7`; crypto_alt avg `-0.005` n `223`; crypto_major avg `0.0603` n `7`; equity avg `0.055` n `47`; fx avg `0.0017` n `4`; index avg `0.0385` n `6`; metal avg `0.1225` n `7`; unknown avg `0.0042` n `312`
- 1h: commodity avg `-0.5559` n `7`; crypto_alt avg `0.307` n `223`; crypto_major avg `0.3142` n `7`; equity avg `0.267` n `47`; fx avg `0.0101` n `4`; index avg `0.2254` n `6`; metal avg `0.5418` n `7`; unknown avg `0.0882` n `312`
- 4h: commodity avg `-0.2938` n `7`; crypto_alt avg `0.1197` n `223`; crypto_major avg `0.4557` n `7`; equity avg `0.3793` n `47`; fx avg `0.0699` n `4`; index avg `0.084` n `6`; metal avg `0.534` n `7`; unknown avg `-0.0915` n `312`
- 24h: commodity avg `0.2465` n `7`; crypto_alt avg `2.3713` n `223`; crypto_major avg `2.332` n `7`; equity avg `0.8148` n `47`; fx avg `0.0701` n `4`; index avg `0.5038` n `6`; metal avg `0.9856` n `7`; unknown avg `-0.1839` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2105`, n `355`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2033`, n `355`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `355`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `355`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.109`, n `355`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `355`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `355`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `355`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0981`, n `351`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `355`, weak_sample_signal
