# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T15:07:27.461289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `1.5428` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.02` n `13`; crypto_alt avg `0.4756` n `238`; crypto_major avg `0.4889` n `8`; equity avg `-0.1202` n `156`; fx avg `-0.0235` n `6`; index avg `-0.0337` n `27`; metal avg `-0.0624` n `20`; unknown avg `159.548` n `1255`
- 1h: commodity avg `-0.0717` n `13`; crypto_alt avg `0.9529` n `238`; crypto_major avg `0.8708` n `8`; equity avg `-0.672` n `156`; fx avg `0.0127` n `6`; index avg `-0.0159` n `27`; metal avg `0.0873` n `20`; unknown avg `0.3517` n `1171`
- 4h: commodity avg `-0.0824` n `13`; crypto_alt avg `0.1657` n `238`; crypto_major avg `-0.3061` n `8`; equity avg `-0.8872` n `156`; fx avg `-0.1094` n `6`; index avg `-0.0354` n `27`; metal avg `-0.2992` n `20`; unknown avg `0.0126` n `1147`
- 24h: commodity avg `0.7348` n `13`; crypto_alt avg `-4.5892` n `238`; crypto_major avg `-3.5999` n `8`; equity avg `-5.2168` n `156`; fx avg `-0.1069` n `6`; index avg `-0.4373` n `27`; metal avg `-0.8638` n `20`; unknown avg `60.5639` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1655`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1486`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
