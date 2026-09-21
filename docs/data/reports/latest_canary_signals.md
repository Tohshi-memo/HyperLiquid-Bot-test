# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T15:07:38.711316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.0937` n `234`; crypto_major avg `0.2976` n `8`; equity avg `0.1939` n `140`; fx avg `0.0074` n `6`; index avg `0.0358` n `26`; metal avg `0.016` n `20`; unknown avg `0.8191` n `940`
- 1h: commodity avg `-0.0642` n `12`; crypto_alt avg `1.2516` n `234`; crypto_major avg `1.4342` n `8`; equity avg `0.5033` n `140`; fx avg `0.0161` n `6`; index avg `0.1297` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.6892` n `904`
- 4h: commodity avg `-0.223` n `12`; crypto_alt avg `0.4821` n `234`; crypto_major avg `1.3548` n `8`; equity avg `0.7154` n `140`; fx avg `0.023` n `6`; index avg `0.1718` n `26`; metal avg `0.0752` n `20`; unknown avg `11.5071` n `856`
- 24h: commodity avg `-0.9595` n `12`; crypto_alt avg `7.1752` n `234`; crypto_major avg `6.7055` n `8`; equity avg `2.669` n `140`; fx avg `-0.0874` n `6`; index avg `0.5268` n `26`; metal avg `0.039` n `20`; unknown avg `8.3643` n `707`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
