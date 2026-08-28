# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T09:07:25.694098+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0662` n `12`; crypto_alt avg `0.0943` n `231`; crypto_major avg `-0.1199` n `8`; equity avg `-0.0468` n `127`; fx avg `0.0054` n `6`; index avg `0.0008` n `26`; metal avg `0.0651` n `20`; unknown avg `-0.042` n `792`
- 1h: commodity avg `0.056` n `12`; crypto_alt avg `-0.2474` n `231`; crypto_major avg `-0.4377` n `8`; equity avg `0.0036` n `127`; fx avg `-0.0053` n `6`; index avg `0.0113` n `26`; metal avg `0.0171` n `20`; unknown avg `-0.1011` n `792`
- 4h: commodity avg `-0.054` n `12`; crypto_alt avg `-0.2122` n `231`; crypto_major avg `-0.271` n `8`; equity avg `-0.4012` n `127`; fx avg `-0.0555` n `6`; index avg `-0.0339` n `26`; metal avg `0.4214` n `20`; unknown avg `-0.0192` n `760`
- 24h: commodity avg `0.2848` n `12`; crypto_alt avg `-1.3196` n `231`; crypto_major avg `-0.459` n `8`; equity avg `-1.1238` n `127`; fx avg `-0.0744` n `6`; index avg `-0.0209` n `26`; metal avg `0.6468` n `20`; unknown avg `0.2932` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
