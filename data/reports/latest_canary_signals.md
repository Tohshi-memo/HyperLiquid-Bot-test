# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T17:08:11.680069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `13`; crypto_alt avg `0.0879` n `239`; crypto_major avg `0.0845` n `8`; equity avg `0.3172` n `158`; fx avg `0.0077` n `6`; index avg `0.031` n `27`; metal avg `0.0376` n `20`; unknown avg `-0.1606` n `1257`
- 1h: commodity avg `0.0212` n `13`; crypto_alt avg `-0.0907` n `239`; crypto_major avg `0.0185` n `8`; equity avg `-0.2502` n `158`; fx avg `0.0244` n `6`; index avg `-0.0407` n `27`; metal avg `-0.0474` n `20`; unknown avg `-0.2199` n `1257`
- 4h: commodity avg `-0.3975` n `13`; crypto_alt avg `0.1664` n `239`; crypto_major avg `0.5355` n `8`; equity avg `1.0042` n `158`; fx avg `0.0593` n `6`; index avg `0.1006` n `27`; metal avg `-0.0905` n `20`; unknown avg `14.5193` n `1251`
- 24h: commodity avg `-0.0565` n `13`; crypto_alt avg `0.0496` n `239`; crypto_major avg `0.7447` n `8`; equity avg `-0.5208` n `158`; fx avg `0.0492` n `6`; index avg `-0.0784` n `27`; metal avg `-0.643` n `20`; unknown avg `0.0975` n `1021`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
