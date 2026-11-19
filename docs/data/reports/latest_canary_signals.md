# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T07:37:26.672822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `-0.0807` n `239`; crypto_major avg `-0.049` n `8`; equity avg `-0.1172` n `164`; fx avg `0.0206` n `6`; index avg `0.0029` n `27`; metal avg `-0.0688` n `20`; unknown avg `11.1091` n `1266`
- 1h: commodity avg `-0.0027` n `13`; crypto_alt avg `0.0148` n `239`; crypto_major avg `0.0043` n `8`; equity avg `0.3742` n `164`; fx avg `0.0533` n `6`; index avg `0.0545` n `27`; metal avg `-0.0066` n `20`; unknown avg `-0.0379` n `1258`
- 4h: commodity avg `0.0973` n `13`; crypto_alt avg `0.5506` n `239`; crypto_major avg `1.3128` n `8`; equity avg `1.3202` n `164`; fx avg `0.0715` n `6`; index avg `0.2241` n `27`; metal avg `0.2375` n `20`; unknown avg `14.9419` n `1214`
- 24h: commodity avg `0.2782` n `13`; crypto_alt avg `0.1924` n `239`; crypto_major avg `-0.4923` n `8`; equity avg `0.382` n `164`; fx avg `-0.0026` n `6`; index avg `0.2134` n `27`; metal avg `-0.2917` n `20`; unknown avg `93.9747` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
