# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T10:52:31.697489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `0.2339` n `235`; crypto_major avg `0.1236` n `8`; equity avg `0.0295` n `144`; fx avg `-0.019` n `6`; index avg `0.0144` n `26`; metal avg `0.0263` n `20`; unknown avg `-0.1752` n `1079`
- 1h: commodity avg `0.0428` n `13`; crypto_alt avg `0.0775` n `235`; crypto_major avg `0.0789` n `8`; equity avg `0.0054` n `144`; fx avg `0.0052` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0343` n `20`; unknown avg `44.0342` n `1077`
- 4h: commodity avg `0.1827` n `13`; crypto_alt avg `0.2378` n `235`; crypto_major avg `0.1741` n `8`; equity avg `-0.1381` n `144`; fx avg `0.0387` n `6`; index avg `-0.0245` n `26`; metal avg `0.0722` n `20`; unknown avg `8.392` n `997`
- 24h: commodity avg `-0.0847` n `13`; crypto_alt avg `1.0475` n `235`; crypto_major avg `0.96` n `8`; equity avg `0.0796` n `144`; fx avg `-0.0627` n `6`; index avg `-0.0832` n `26`; metal avg `0.229` n `20`; unknown avg `0.6713` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2101`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
