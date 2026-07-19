# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T07:18:30.296978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `-0.0306` n `230`; crypto_major avg `-0.0287` n `8`; equity avg `-0.0077` n `96`; fx avg `0.0148` n `6`; index avg `0.0238` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0236` n `770`
- 1h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0046` n `230`; crypto_major avg `-0.0459` n `8`; equity avg `0.0193` n `96`; fx avg `0.008` n `6`; index avg `0.0259` n `25`; metal avg `0.0054` n `20`; unknown avg `-0.0665` n `770`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.1219` n `230`; crypto_major avg `0.1046` n `8`; equity avg `0.1602` n `96`; fx avg `0.0247` n `6`; index avg `-0.0056` n `25`; metal avg `0.0009` n `20`; unknown avg `0.0111` n `752`
- 24h: commodity avg `0.2976` n `12`; crypto_alt avg `0.2969` n `230`; crypto_major avg `0.9578` n `8`; equity avg `0.0586` n `96`; fx avg `-0.0025` n `6`; index avg `0.0062` n `25`; metal avg `-0.0161` n `20`; unknown avg `0.0565` n `751`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
