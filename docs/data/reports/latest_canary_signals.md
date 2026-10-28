# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T05:37:27.619356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0398` n `13`; crypto_alt avg `-0.0852` n `238`; crypto_major avg `-0.0866` n `8`; equity avg `-0.0805` n `154`; fx avg `-0.0212` n `6`; index avg `0.0011` n `27`; metal avg `-0.0077` n `20`; unknown avg `0.0902` n `1238`
- 1h: commodity avg `0.0215` n `13`; crypto_alt avg `-0.0619` n `238`; crypto_major avg `-0.1321` n `8`; equity avg `0.1657` n `154`; fx avg `-0.0401` n `6`; index avg `0.0329` n `27`; metal avg `-0.0276` n `20`; unknown avg `79.5068` n `1234`
- 4h: commodity avg `0.0498` n `13`; crypto_alt avg `-0.0838` n `238`; crypto_major avg `-0.0989` n `8`; equity avg `0.52` n `154`; fx avg `-0.0078` n `6`; index avg `0.0097` n `27`; metal avg `-0.1688` n `20`; unknown avg `50.8494` n `1214`
- 24h: commodity avg `0.0606` n `13`; crypto_alt avg `2.208` n `237`; crypto_major avg `2.0678` n `8`; equity avg `3.711` n `154`; fx avg `0.0828` n `6`; index avg `0.5042` n `27`; metal avg `0.224` n `20`; unknown avg `16.1873` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
