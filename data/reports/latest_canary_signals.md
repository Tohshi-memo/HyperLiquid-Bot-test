# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T16:52:27.514643+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.451` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0318` n `13`; crypto_alt avg `0.0601` n `239`; crypto_major avg `-0.1313` n `8`; equity avg `0.167` n `168`; fx avg `-0.0023` n `6`; index avg `0.0349` n `27`; metal avg `0.0512` n `20`; unknown avg `1.4535` n `1256`
- 1h: commodity avg `-0.1738` n `13`; crypto_alt avg `0.4553` n `239`; crypto_major avg `0.3957` n `8`; equity avg `0.656` n `168`; fx avg `-0.018` n `6`; index avg `0.0682` n `27`; metal avg `0.034` n `20`; unknown avg `1.0739` n `1244`
- 4h: commodity avg `-0.3559` n `13`; crypto_alt avg `-1.3159` n `239`; crypto_major avg `-1.4402` n `8`; equity avg `-0.2396` n `168`; fx avg `-0.0855` n `6`; index avg `0.0108` n `27`; metal avg `-0.2978` n `20`; unknown avg `0.7442` n `1245`
- 24h: commodity avg `-0.4909` n `13`; crypto_alt avg `0.7542` n `239`; crypto_major avg `1.3843` n `8`; equity avg `3.3134` n `168`; fx avg `-0.1429` n `6`; index avg `0.3194` n `27`; metal avg `0.7288` n `20`; unknown avg `191.5759` n `1035`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
