# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T05:22:26.922556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0062` n `13`; crypto_alt avg `0.1009` n `239`; crypto_major avg `0.1915` n `8`; equity avg `0.0352` n `162`; fx avg `-0.0044` n `6`; index avg `0.0177` n `27`; metal avg `0.0618` n `20`; unknown avg `-0.0039` n `1264`
- 1h: commodity avg `0.0302` n `13`; crypto_alt avg `0.0196` n `239`; crypto_major avg `0.2302` n `8`; equity avg `-0.0103` n `162`; fx avg `-0.0096` n `6`; index avg `0.0136` n `27`; metal avg `0.1019` n `20`; unknown avg `0.4368` n `1260`
- 4h: commodity avg `-0.1705` n `13`; crypto_alt avg `1.133` n `239`; crypto_major avg `1.0788` n `8`; equity avg `0.0799` n `162`; fx avg `-0.0483` n `6`; index avg `-0.0342` n `27`; metal avg `0.2877` n `20`; unknown avg `0.4359` n `1244`
- 24h: commodity avg `-1.1445` n `13`; crypto_alt avg `0.676` n `239`; crypto_major avg `1.2951` n `8`; equity avg `-2.5314` n `162`; fx avg `-0.0466` n `6`; index avg `-0.2521` n `27`; metal avg `-0.0666` n `20`; unknown avg `559.9587` n `985`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
