# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T20:15:26.289750+00:00`
- Correlation status: `ready`
- Asset price records: `200`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.05` n `7`; crypto_alt avg `0.025` n `223`; crypto_major avg `-0.0628` n `7`; equity avg `0.0037` n `42`; fx avg `0.0242` n `4`; index avg `-0.002` n `9`; metal avg `-0.0353` n `7`; unknown avg `0.0264` n `314`
- 1h: commodity avg `0.009` n `7`; crypto_alt avg `0.095` n `223`; crypto_major avg `0.0845` n `7`; equity avg `0.0217` n `42`; fx avg `0.0388` n `4`; index avg `0.0096` n `9`; metal avg `0.0081` n `7`; unknown avg `-0.0081` n `314`
- 4h: commodity avg `0.448` n `7`; crypto_alt avg `0.4451` n `223`; crypto_major avg `0.2299` n `7`; equity avg `0.1468` n `42`; fx avg `0.0001` n `4`; index avg `0.013` n `9`; metal avg `0.1254` n `7`; unknown avg `0.1711` n `313`
- 24h: commodity avg `0.0137` n `7`; crypto_alt avg `-0.1683` n `223`; crypto_major avg `0.1732` n `7`; equity avg `0.3076` n `42`; fx avg `0.0783` n `4`; index avg `0.0583` n `9`; metal avg `0.4709` n `7`; unknown avg `0.0646` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3987`, n `196`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3809`, n `196`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3788`, n `192`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3715`, n `192`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3714`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3584`, n `196`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3329`, n `196`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3144`, n `196`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3058`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2503`, n `192`, moderate_sample_signal
