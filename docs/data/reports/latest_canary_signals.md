# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T19:22:36.548068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0447` n `13`; crypto_alt avg `-0.354` n `234`; crypto_major avg `-0.2336` n `8`; equity avg `-0.0097` n `142`; fx avg `0.0031` n `6`; index avg `0.0045` n `26`; metal avg `0.0623` n `20`; unknown avg `2.9133` n `975`
- 1h: commodity avg `0.0493` n `13`; crypto_alt avg `-0.3476` n `234`; crypto_major avg `-0.1799` n `8`; equity avg `0.181` n `142`; fx avg `0.0175` n `6`; index avg `0.0543` n `26`; metal avg `0.0697` n `20`; unknown avg `0.5996` n `973`
- 4h: commodity avg `-0.044` n `13`; crypto_alt avg `0.3025` n `234`; crypto_major avg `0.0924` n `8`; equity avg `1.0002` n `142`; fx avg `-0.0337` n `6`; index avg `0.2007` n `26`; metal avg `0.1437` n `20`; unknown avg `1.1935` n `967`
- 24h: commodity avg `0.0449` n `13`; crypto_alt avg `-0.0289` n `234`; crypto_major avg `0.1693` n `8`; equity avg `0.8885` n `142`; fx avg `-0.0934` n `6`; index avg `0.1398` n `26`; metal avg `-0.0113` n `20`; unknown avg `0.5186` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
