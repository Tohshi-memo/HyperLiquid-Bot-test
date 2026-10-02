# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T12:22:37.231284+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0397` n `13`; crypto_alt avg `0.2688` n `234`; crypto_major avg `0.1105` n `8`; equity avg `0.087` n `142`; fx avg `0.0035` n `6`; index avg `0.0328` n `26`; metal avg `-0.0226` n `20`; unknown avg `-0.038` n `985`
- 1h: commodity avg `0.0693` n `13`; crypto_alt avg `0.276` n `234`; crypto_major avg `-0.013` n `8`; equity avg `-0.0781` n `142`; fx avg `-0.0277` n `6`; index avg `-0.0118` n `26`; metal avg `-0.0963` n `20`; unknown avg `-0.1576` n `977`
- 4h: commodity avg `-0.0767` n `13`; crypto_alt avg `0.0651` n `234`; crypto_major avg `-0.0738` n `8`; equity avg `-0.3168` n `142`; fx avg `-0.0337` n `6`; index avg `0.0021` n `26`; metal avg `-0.1621` n `20`; unknown avg `0.1181` n `975`
- 24h: commodity avg `-0.5307` n `13`; crypto_alt avg `2.1502` n `234`; crypto_major avg `1.9345` n `8`; equity avg `0.9559` n `142`; fx avg `-0.3447` n `6`; index avg `0.1813` n `26`; metal avg `-0.1508` n `20`; unknown avg `-0.089` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
