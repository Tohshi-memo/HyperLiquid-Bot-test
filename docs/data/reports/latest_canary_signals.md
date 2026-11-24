# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T15:52:32.145471+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2159` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1683` n `13`; crypto_alt avg `-0.1599` n `239`; crypto_major avg `-0.0965` n `8`; equity avg `-0.5711` n `168`; fx avg `-0.0007` n `6`; index avg `-0.0543` n `27`; metal avg `-0.1117` n `20`; unknown avg `154.7019` n `1265`
- 1h: commodity avg `-0.3606` n `13`; crypto_alt avg `-1.2555` n `239`; crypto_major avg `-1.0074` n `8`; equity avg `-2.0947` n `168`; fx avg `-0.0022` n `6`; index avg `-0.2003` n `27`; metal avg `-0.5793` n `20`; unknown avg `-0.4262` n `1259`
- 4h: commodity avg `0.0106` n `13`; crypto_alt avg `-1.608` n `239`; crypto_major avg `-1.3954` n `8`; equity avg `-2.2206` n `167`; fx avg `0.0438` n `6`; index avg `-0.1795` n `27`; metal avg `-0.5175` n `20`; unknown avg `160.7996` n `1243`
- 24h: commodity avg `0.3639` n `13`; crypto_alt avg `-5.1683` n `239`; crypto_major avg `-5.5492` n `8`; equity avg `-5.0658` n `167`; fx avg `0.1907` n `6`; index avg `-0.3773` n `27`; metal avg `-1.2037` n `20`; unknown avg `-0.6715` n `1137`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
