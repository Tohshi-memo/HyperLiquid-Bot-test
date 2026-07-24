# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T04:07:24.070473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0412` n `12`; crypto_alt avg `0.0088` n `230`; crypto_major avg `-0.0331` n `8`; equity avg `-0.0349` n `100`; fx avg `-0.0134` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0314` n `20`; unknown avg `-0.0386` n `772`
- 1h: commodity avg `-0.0254` n `12`; crypto_alt avg `0.2662` n `230`; crypto_major avg `0.2486` n `8`; equity avg `-0.098` n `100`; fx avg `-0.0055` n `6`; index avg `0.0183` n `25`; metal avg `0.0202` n `20`; unknown avg `1.4883` n `772`
- 4h: commodity avg `-0.0653` n `12`; crypto_alt avg `0.6019` n `230`; crypto_major avg `0.4757` n `8`; equity avg `-0.6786` n `100`; fx avg `-0.0957` n `6`; index avg `-0.2287` n `25`; metal avg `-0.1583` n `20`; unknown avg `0.6138` n `772`
- 24h: commodity avg `0.4932` n `12`; crypto_alt avg `-0.7692` n `230`; crypto_major avg `-1.5066` n `8`; equity avg `-2.0198` n `99`; fx avg `-0.1108` n `6`; index avg `-0.5507` n `25`; metal avg `-1.0381` n `20`; unknown avg `-0.2334` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1102`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1002`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
