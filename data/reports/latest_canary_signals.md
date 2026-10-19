# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T11:22:29.991175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0533` n `13`; crypto_alt avg `-0.1516` n `237`; crypto_major avg `-0.0297` n `8`; equity avg `-0.0089` n `151`; fx avg `0.0078` n `6`; index avg `0.0037` n `26`; metal avg `0.0307` n `20`; unknown avg `0.0407` n `1195`
- 1h: commodity avg `-0.0141` n `13`; crypto_alt avg `-0.6145` n `237`; crypto_major avg `-0.3878` n `8`; equity avg `0.0408` n `151`; fx avg `0.0221` n `6`; index avg `0.0115` n `26`; metal avg `0.099` n `20`; unknown avg `0.1096` n `1193`
- 4h: commodity avg `0.3706` n `13`; crypto_alt avg `-1.1002` n `237`; crypto_major avg `-0.8308` n `8`; equity avg `-0.0521` n `151`; fx avg `0.031` n `6`; index avg `-0.0177` n `26`; metal avg `0.0031` n `20`; unknown avg `0.3486` n `1149`
- 24h: commodity avg `-0.0872` n `13`; crypto_alt avg `-0.878` n `237`; crypto_major avg `-0.0007` n `8`; equity avg `2.4688` n `151`; fx avg `-0.0294` n `6`; index avg `0.4474` n `26`; metal avg `0.3095` n `20`; unknown avg `1.2107` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1994`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0595`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
