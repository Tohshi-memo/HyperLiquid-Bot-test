# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T10:52:27.532000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1327` n `13`; crypto_alt avg `0.1079` n `239`; crypto_major avg `0.0379` n `8`; equity avg `0.1112` n `162`; fx avg `-0.0083` n `6`; index avg `0.0134` n `27`; metal avg `-0.0161` n `20`; unknown avg `0.0185` n `1260`
- 1h: commodity avg `0.0367` n `13`; crypto_alt avg `0.1661` n `239`; crypto_major avg `0.3001` n `8`; equity avg `0.2715` n `162`; fx avg `-0.0217` n `6`; index avg `0.0359` n `27`; metal avg `-0.0254` n `20`; unknown avg `207.1419` n `1206`
- 4h: commodity avg `-0.037` n `13`; crypto_alt avg `0.5117` n `239`; crypto_major avg `0.8535` n `8`; equity avg `0.5156` n `162`; fx avg `-0.0115` n `6`; index avg `0.0691` n `27`; metal avg `-0.0829` n `20`; unknown avg `218.5078` n `1148`
- 24h: commodity avg `0.7761` n `13`; crypto_alt avg `-0.9496` n `239`; crypto_major avg `-2.7797` n `8`; equity avg `-1.125` n `162`; fx avg `-0.0548` n `6`; index avg `0.0347` n `27`; metal avg `-0.4859` n `20`; unknown avg `232.5989` n `1075`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
