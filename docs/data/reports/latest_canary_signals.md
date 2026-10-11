# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T19:22:28.033252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0056` n `13`; crypto_alt avg `0.1456` n `235`; crypto_major avg `0.1108` n `8`; equity avg `0.016` n `150`; fx avg `0.0008` n `6`; index avg `0.0039` n `26`; metal avg `0.0064` n `20`; unknown avg `-0.0517` n `1134`
- 1h: commodity avg `0.0272` n `13`; crypto_alt avg `0.051` n `235`; crypto_major avg `-0.1796` n `8`; equity avg `-0.0269` n `150`; fx avg `0.0007` n `6`; index avg `-0.006` n `26`; metal avg `0.0033` n `20`; unknown avg `-0.2106` n `1122`
- 4h: commodity avg `0.0635` n `13`; crypto_alt avg `1.0277` n `235`; crypto_major avg `0.8006` n `8`; equity avg `0.2` n `150`; fx avg `-0.0011` n `6`; index avg `0.0308` n `26`; metal avg `0.0449` n `20`; unknown avg `1.6042` n `1092`
- 24h: commodity avg `0.2833` n `13`; crypto_alt avg `1.8947` n `235`; crypto_major avg `0.7096` n `8`; equity avg `0.2844` n `150`; fx avg `0.0178` n `6`; index avg `0.0426` n `26`; metal avg `0.0762` n `20`; unknown avg `0.7967` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
