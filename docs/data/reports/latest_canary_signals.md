# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T20:22:29.063067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `13`; crypto_alt avg `-0.051` n `235`; crypto_major avg `-0.1211` n `8`; equity avg `-0.0066` n `150`; fx avg `-0.0014` n `6`; index avg `0.0008` n `26`; metal avg `-0.001` n `20`; unknown avg `0.7333` n `1117`
- 1h: commodity avg `0.0014` n `13`; crypto_alt avg `0.0008` n `235`; crypto_major avg `-0.0901` n `8`; equity avg `0.0153` n `150`; fx avg `-0.0023` n `6`; index avg `0.0089` n `26`; metal avg `-0.0016` n `20`; unknown avg `2.7917` n `1085`
- 4h: commodity avg `0.0835` n `13`; crypto_alt avg `0.2203` n `235`; crypto_major avg `-0.1147` n `8`; equity avg `-0.0083` n `150`; fx avg `-0.0045` n `6`; index avg `-0.0137` n `26`; metal avg `-0.006` n `20`; unknown avg `2.7028` n `999`
- 24h: commodity avg `-0.1644` n `13`; crypto_alt avg `2.9129` n `235`; crypto_major avg `1.1082` n `8`; equity avg `0.1678` n `150`; fx avg `-0.0121` n `6`; index avg `0.02` n `26`; metal avg `-0.0358` n `20`; unknown avg `0.4446` n `964`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
