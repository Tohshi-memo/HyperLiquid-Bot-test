# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T02:22:30.110583+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3617` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0176` n `13`; crypto_alt avg `-0.1487` n `239`; crypto_major avg `0.1079` n `8`; equity avg `0.2216` n `165`; fx avg `-0.0099` n `6`; index avg `0.066` n `27`; metal avg `-0.0596` n `20`; unknown avg `3.5797` n `1260`
- 1h: commodity avg `-0.0172` n `13`; crypto_alt avg `-1.4667` n `239`; crypto_major avg `-1.3637` n `8`; equity avg `-0.4078` n `165`; fx avg `-0.0059` n `6`; index avg `-0.002` n `27`; metal avg `-0.3157` n `20`; unknown avg `162.7285` n `1258`
- 4h: commodity avg `-0.1025` n `13`; crypto_alt avg `-1.2798` n `239`; crypto_major avg `-0.9843` n `8`; equity avg `-1.4322` n `165`; fx avg `0.0007` n `6`; index avg `-0.0983` n `27`; metal avg `-0.7973` n `20`; unknown avg `17.5161` n `1250`
- 24h: commodity avg `-0.1167` n `13`; crypto_alt avg `-2.7165` n `239`; crypto_major avg `-1.8031` n `8`; equity avg `-5.3657` n `165`; fx avg `0.0133` n `6`; index avg `-0.3703` n `27`; metal avg `-1.7698` n `20`; unknown avg `2.5121` n `1170`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
