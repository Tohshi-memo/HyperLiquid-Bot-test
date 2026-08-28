# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T12:37:31.109391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.1945` n `231`; crypto_major avg `-0.2836` n `8`; equity avg `-0.0365` n `127`; fx avg `-0.0066` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0087` n `20`; unknown avg `-0.0439` n `792`
- 1h: commodity avg `-0.1426` n `12`; crypto_alt avg `-0.2921` n `231`; crypto_major avg `-0.4017` n `8`; equity avg `-0.0415` n `127`; fx avg `-0.0257` n `6`; index avg `0.0083` n `26`; metal avg `0.044` n `20`; unknown avg `0.209` n `792`
- 4h: commodity avg `-0.1157` n `12`; crypto_alt avg `-0.1091` n `231`; crypto_major avg `-0.7527` n `8`; equity avg `-0.1116` n `127`; fx avg `0.037` n `6`; index avg `-0.0078` n `26`; metal avg `0.1602` n `20`; unknown avg `0.1481` n `792`
- 24h: commodity avg `-0.1278` n `12`; crypto_alt avg `-0.3271` n `231`; crypto_major avg `-0.0194` n `8`; equity avg `-0.8753` n `127`; fx avg `-0.054` n `6`; index avg `-0.0124` n `26`; metal avg `0.8132` n `20`; unknown avg `0.5394` n `760`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
