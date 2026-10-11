# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T15:52:29.192866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0506` n `13`; crypto_alt avg `0.271` n `235`; crypto_major avg `0.4101` n `8`; equity avg `0.0548` n `150`; fx avg `0.0018` n `6`; index avg `0.008` n `26`; metal avg `0.0043` n `20`; unknown avg `1.9952` n `1134`
- 1h: commodity avg `0.141` n `13`; crypto_alt avg `0.6462` n `235`; crypto_major avg `0.6792` n `8`; equity avg `0.0889` n `150`; fx avg `0.0007` n `6`; index avg `0.0082` n `26`; metal avg `0.0048` n `20`; unknown avg `1.8479` n `1132`
- 4h: commodity avg `0.0091` n `13`; crypto_alt avg `1.732` n `235`; crypto_major avg `0.8773` n `8`; equity avg `0.1517` n `150`; fx avg `-0.01` n `6`; index avg `0.021` n `26`; metal avg `0.0199` n `20`; unknown avg `2.8719` n `1053`
- 24h: commodity avg `0.2754` n `13`; crypto_alt avg `1.8176` n `235`; crypto_major avg `0.3945` n `8`; equity avg `0.1409` n `150`; fx avg `0.0143` n `6`; index avg `-0.0006` n `26`; metal avg `0.0369` n `20`; unknown avg `1.4926` n `941`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
