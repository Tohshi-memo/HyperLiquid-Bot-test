# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T09:52:28.263808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0245` n `13`; crypto_alt avg `0.1171` n `235`; crypto_major avg `0.0945` n `8`; equity avg `0.0331` n `151`; fx avg `-0.0185` n `6`; index avg `0.0089` n `26`; metal avg `0.0377` n `20`; unknown avg `0.1589` n `1133`
- 1h: commodity avg `0.123` n `13`; crypto_alt avg `-0.0892` n `235`; crypto_major avg `-0.1153` n `8`; equity avg `0.0801` n `151`; fx avg `0.0003` n `6`; index avg `-0.0128` n `26`; metal avg `0.0699` n `20`; unknown avg `-0.0453` n `1055`
- 4h: commodity avg `0.3351` n `13`; crypto_alt avg `-0.8631` n `235`; crypto_major avg `-0.5967` n `8`; equity avg `-0.6878` n `151`; fx avg `-0.0678` n `6`; index avg `-0.1067` n `26`; metal avg `-0.0603` n `20`; unknown avg `0.5003` n `981`
- 24h: commodity avg `-0.0459` n `13`; crypto_alt avg `1.9847` n `235`; crypto_major avg `1.3218` n `8`; equity avg `-1.0691` n `151`; fx avg `-0.1118` n `6`; index avg `-0.1291` n `26`; metal avg `0.0222` n `20`; unknown avg `0.1505` n `838`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
