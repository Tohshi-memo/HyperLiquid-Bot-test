# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T23:07:22.146597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.2896` n `230`; crypto_major avg `-0.216` n `8`; equity avg `-0.134` n `98`; fx avg `-0.0003` n `6`; index avg `0.006` n `25`; metal avg `-0.0201` n `20`; unknown avg `-0.0455` n `769`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.2516` n `230`; crypto_major avg `0.1871` n `8`; equity avg `0.1747` n `98`; fx avg `0.0028` n `6`; index avg `0.0623` n `25`; metal avg `0.0129` n `20`; unknown avg `-0.2026` n `769`
- 4h: commodity avg `-0.0103` n `12`; crypto_alt avg `0.2645` n `230`; crypto_major avg `0.2037` n `8`; equity avg `0.1659` n `98`; fx avg `0.015` n `6`; index avg `0.0661` n `25`; metal avg `-0.1216` n `20`; unknown avg `-0.023` n `769`
- 24h: commodity avg `-0.1021` n `12`; crypto_alt avg `-0.1753` n `230`; crypto_major avg `0.1467` n `8`; equity avg `0.4857` n `97`; fx avg `0.0797` n `6`; index avg `0.0086` n `25`; metal avg `-0.0934` n `20`; unknown avg `-0.1237` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1411`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1362`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1268`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0967`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0953`, n `666`, weak_sample_signal
