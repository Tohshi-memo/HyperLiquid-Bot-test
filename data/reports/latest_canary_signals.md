# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T04:07:26.564059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0497` n `13`; crypto_alt avg `0.0992` n `234`; crypto_major avg `0.187` n `8`; equity avg `0.0327` n `142`; fx avg `-0.0047` n `6`; index avg `0.0152` n `26`; metal avg `0.0754` n `20`; unknown avg `-0.0787` n `977`
- 1h: commodity avg `-0.0089` n `13`; crypto_alt avg `-0.0973` n `234`; crypto_major avg `0.2499` n `8`; equity avg `-0.0268` n `142`; fx avg `-0.0041` n `6`; index avg `0.0118` n `26`; metal avg `0.0907` n `20`; unknown avg `0.2278` n `977`
- 4h: commodity avg `-0.1706` n `13`; crypto_alt avg `0.5468` n `234`; crypto_major avg `0.8478` n `8`; equity avg `0.1468` n `142`; fx avg `-0.0375` n `6`; index avg `0.0669` n `26`; metal avg `0.0501` n `20`; unknown avg `1.2287` n `977`
- 24h: commodity avg `0.5682` n `13`; crypto_alt avg `-0.6882` n `234`; crypto_major avg `0.7027` n `8`; equity avg `0.3797` n `142`; fx avg `-0.2258` n `6`; index avg `0.0249` n `26`; metal avg `-0.0621` n `20`; unknown avg `0.3803` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
