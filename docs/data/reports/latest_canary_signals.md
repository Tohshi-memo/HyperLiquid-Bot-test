# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T06:07:38.971118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `13`; crypto_alt avg `0.1568` n `234`; crypto_major avg `0.1187` n `8`; equity avg `0.0873` n `142`; fx avg `-0.043` n `6`; index avg `0.0258` n `26`; metal avg `0.0692` n `20`; unknown avg `-0.0093` n `951`
- 1h: commodity avg `0.0381` n `13`; crypto_alt avg `-0.1924` n `234`; crypto_major avg `-0.2933` n `8`; equity avg `-0.0358` n `142`; fx avg `-0.0776` n `6`; index avg `0.0043` n `26`; metal avg `0.0427` n `20`; unknown avg `0.3091` n `951`
- 4h: commodity avg `-0.0495` n `13`; crypto_alt avg `1.1079` n `234`; crypto_major avg `1.1948` n `8`; equity avg `0.2298` n `142`; fx avg `-0.1044` n `6`; index avg `0.0443` n `26`; metal avg `0.3259` n `20`; unknown avg `0.8345` n `945`
- 24h: commodity avg `0.2899` n `13`; crypto_alt avg `0.1227` n `234`; crypto_major avg `0.863` n `8`; equity avg `-0.0331` n `142`; fx avg `-0.3049` n `6`; index avg `-0.0583` n `26`; metal avg `-0.1249` n `20`; unknown avg `584.8646` n `838`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
