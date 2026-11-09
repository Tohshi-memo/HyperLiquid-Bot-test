# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T08:37:27.902683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2608` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0262` n `13`; crypto_alt avg `0.0441` n `239`; crypto_major avg `0.0657` n `8`; equity avg `0.2014` n `158`; fx avg `0.0368` n `6`; index avg `0.0293` n `27`; metal avg `0.052` n `20`; unknown avg `-0.0411` n `1249`
- 1h: commodity avg `0.0497` n `13`; crypto_alt avg `0.4212` n `239`; crypto_major avg `0.2834` n `8`; equity avg `0.504` n `158`; fx avg `0.0835` n `6`; index avg `0.0652` n `27`; metal avg `0.0813` n `20`; unknown avg `0.1048` n `1147`
- 4h: commodity avg `-0.4354` n `13`; crypto_alt avg `-1.3088` n `239`; crypto_major avg `-1.4128` n `8`; equity avg `-1.21` n `158`; fx avg `0.0099` n `6`; index avg `-0.152` n `27`; metal avg `-0.3119` n `20`; unknown avg `0.1112` n `1119`
- 24h: commodity avg `-0.4434` n `13`; crypto_alt avg `-2.7193` n `239`; crypto_major avg `-3.5348` n `8`; equity avg `-0.7793` n `158`; fx avg `-0.0815` n `6`; index avg `-0.1147` n `27`; metal avg `0.2538` n `20`; unknown avg `0.2242` n `952`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
