# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T01:07:26.870515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1044` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `-0.4434` n `239`; crypto_major avg `-0.3934` n `8`; equity avg `-0.2004` n `161`; fx avg `-0.0039` n `6`; index avg `-0.0311` n `27`; metal avg `0.1018` n `20`; unknown avg `20.1601` n `1258`
- 1h: commodity avg `-0.0635` n `13`; crypto_alt avg `-0.2861` n `239`; crypto_major avg `-0.1052` n `8`; equity avg `-0.248` n `161`; fx avg `0.0234` n `6`; index avg `-0.039` n `27`; metal avg `0.2264` n `20`; unknown avg `21.0254` n `1256`
- 4h: commodity avg `-0.0686` n `13`; crypto_alt avg `-1.4267` n `239`; crypto_major avg `-1.2545` n `8`; equity avg `-1.7146` n `161`; fx avg `-0.0582` n `6`; index avg `-0.1501` n `27`; metal avg `0.0819` n `20`; unknown avg `3.1464` n `1240`
- 24h: commodity avg `0.1201` n `13`; crypto_alt avg `-1.2987` n `239`; crypto_major avg `0.1144` n `8`; equity avg `1.687` n `161`; fx avg `-0.1617` n `6`; index avg `0.179` n `27`; metal avg `-0.0236` n `20`; unknown avg `3.6865` n `1141`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
