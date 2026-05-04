# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T03:00:30.362742+00:00`
- Correlation status: `ready`
- Asset price records: `227`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `7`; crypto_alt avg `0.1382` n `223`; crypto_major avg `-0.0197` n `7`; equity avg `0.0939` n `42`; fx avg `-0.0008` n `4`; index avg `0.0887` n `9`; metal avg `0.0696` n `7`; unknown avg `0.069` n `314`
- 1h: commodity avg `0.0757` n `7`; crypto_alt avg `0.7547` n `223`; crypto_major avg `0.5338` n `7`; equity avg `0.4337` n `42`; fx avg `0.0199` n `4`; index avg `0.2428` n `9`; metal avg `-0.0889` n `7`; unknown avg `-0.2098` n `314`
- 4h: commodity avg `0.307` n `7`; crypto_alt avg `1.3849` n `223`; crypto_major avg `1.3475` n `7`; equity avg `1.0394` n `42`; fx avg `0.039` n `4`; index avg `0.6958` n `9`; metal avg `-0.0834` n `7`; unknown avg `0.1205` n `314`
- 24h: commodity avg `0.135` n `7`; crypto_alt avg `2.6102` n `223`; crypto_major avg `2.7083` n `7`; equity avg `1.274` n `42`; fx avg `0.0167` n `4`; index avg `0.7742` n `9`; metal avg `0.3193` n `7`; unknown avg `0.5547` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.38`, n `219`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.373`, n `223`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3722`, n `219`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3574`, n `223`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.2068`, n `219`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2006`, n `219`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1923`, n `223`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1886`, n `223`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1864`, n `223`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `223`, weak_sample_signal
