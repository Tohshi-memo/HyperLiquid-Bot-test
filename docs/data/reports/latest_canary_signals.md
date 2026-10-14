# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T00:22:25.373369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0694` n `13`; crypto_alt avg `0.302` n `235`; crypto_major avg `0.2471` n `8`; equity avg `0.1173` n `151`; fx avg `-0.0173` n `6`; index avg `0.0249` n `26`; metal avg `-0.0056` n `20`; unknown avg `0.3786` n `1135`
- 1h: commodity avg `0.0514` n `13`; crypto_alt avg `0.5055` n `235`; crypto_major avg `0.303` n `8`; equity avg `0.2092` n `151`; fx avg `-0.0391` n `6`; index avg `0.0329` n `26`; metal avg `0.0288` n `20`; unknown avg `3.9562` n `1133`
- 4h: commodity avg `-0.0208` n `13`; crypto_alt avg `0.4015` n `235`; crypto_major avg `0.2308` n `8`; equity avg `0.1809` n `151`; fx avg `-0.0394` n `6`; index avg `0.0174` n `26`; metal avg `0.0044` n `20`; unknown avg `1.6421` n `1065`
- 24h: commodity avg `0.9093` n `13`; crypto_alt avg `2.3857` n `235`; crypto_major avg `2.5551` n `8`; equity avg `0.5782` n `151`; fx avg `0.1408` n `6`; index avg `0.0236` n `26`; metal avg `-0.2108` n `20`; unknown avg `0.5542` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1568`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1161`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.093`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `666`, weak_sample_signal
