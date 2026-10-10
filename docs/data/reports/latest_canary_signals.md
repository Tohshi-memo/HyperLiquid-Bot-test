# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T07:22:26.520250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0138` n `13`; crypto_alt avg `-0.0773` n `235`; crypto_major avg `-0.0148` n `8`; equity avg `0.0131` n `150`; fx avg `0.0` n `6`; index avg `0.0009` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.0084` n `1117`
- 1h: commodity avg `-0.0133` n `13`; crypto_alt avg `-0.1814` n `235`; crypto_major avg `-0.0704` n `8`; equity avg `-0.0205` n `150`; fx avg `-0.005` n `6`; index avg `-0.017` n `26`; metal avg `0.01` n `20`; unknown avg `1.6386` n `1114`
- 4h: commodity avg `0.038` n `13`; crypto_alt avg `-0.0339` n `235`; crypto_major avg `0.1291` n `8`; equity avg `-0.0349` n `150`; fx avg `-0.0008` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0119` n `20`; unknown avg `0.0809` n `1092`
- 24h: commodity avg `-0.025` n `13`; crypto_alt avg `1.2233` n `235`; crypto_major avg `-0.1025` n `8`; equity avg `-0.2229` n `150`; fx avg `-0.0503` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0082` n `20`; unknown avg `666.7517` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
