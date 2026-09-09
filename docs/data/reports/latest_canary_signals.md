# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T20:52:34.348681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0672` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0107` n `12`; crypto_alt avg `-0.1457` n `233`; crypto_major avg `-0.1322` n `8`; equity avg `-0.0056` n `134`; fx avg `0.0004` n `6`; index avg `0.0002` n `26`; metal avg `0.001` n `20`; unknown avg `31.5725` n `797`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0872` n `233`; crypto_major avg `-0.125` n `8`; equity avg `-0.0153` n `134`; fx avg `0.0023` n `6`; index avg `0.0074` n `26`; metal avg `-0.0089` n `20`; unknown avg `27.8428` n `745`
- 4h: commodity avg `0.0416` n `12`; crypto_alt avg `-1.3235` n `233`; crypto_major avg `-1.0729` n `8`; equity avg `-0.3538` n `134`; fx avg `0.0105` n `6`; index avg `-0.0057` n `26`; metal avg `-0.13` n `20`; unknown avg `2.7154` n `745`
- 24h: commodity avg `0.0718` n `12`; crypto_alt avg `-1.3825` n `233`; crypto_major avg `-1.0112` n `8`; equity avg `-0.3481` n `134`; fx avg `-0.0243` n `6`; index avg `-0.1223` n `26`; metal avg `0.5251` n `20`; unknown avg `150.4738` n `705`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
