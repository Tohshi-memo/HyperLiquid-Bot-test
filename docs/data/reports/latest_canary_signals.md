# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T09:37:47.798966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1968` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0817` n `13`; crypto_alt avg `0.0601` n `239`; crypto_major avg `0.2509` n `8`; equity avg `0.0197` n `166`; fx avg `0.0187` n `6`; index avg `0.0188` n `27`; metal avg `0.0264` n `20`; unknown avg `159.1553` n `1266`
- 1h: commodity avg `0.1448` n `13`; crypto_alt avg `-0.6738` n `239`; crypto_major avg `-0.3583` n `8`; equity avg `-0.8775` n `166`; fx avg `0.0367` n `6`; index avg `-0.083` n `27`; metal avg `-0.0691` n `20`; unknown avg `159.4688` n `1256`
- 4h: commodity avg `0.3204` n `13`; crypto_alt avg `-1.6666` n `239`; crypto_major avg `-1.4148` n `8`; equity avg `-1.934` n `166`; fx avg `0.0516` n `6`; index avg `-0.218` n `27`; metal avg `-0.3171` n `20`; unknown avg `333.1655` n `1200`
- 24h: commodity avg `-0.6018` n `13`; crypto_alt avg `-0.8243` n `239`; crypto_major avg `-1.2039` n `8`; equity avg `1.6147` n `166`; fx avg `-0.1542` n `6`; index avg `0.3966` n `27`; metal avg `-0.4439` n `20`; unknown avg `0.4279` n `1142`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
