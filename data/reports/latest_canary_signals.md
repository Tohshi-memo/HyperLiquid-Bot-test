# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T06:07:29.578932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.0523` n `229`; crypto_major avg `-0.0269` n `8`; equity avg `0.1259` n `91`; fx avg `0.005` n `6`; index avg `0.0209` n `25`; metal avg `0.0728` n `20`; unknown avg `-0.0167` n `748`
- 1h: commodity avg `-0.1773` n `12`; crypto_alt avg `0.3939` n `229`; crypto_major avg `0.4199` n `8`; equity avg `0.1455` n `91`; fx avg `0.0292` n `6`; index avg `0.0344` n `25`; metal avg `0.2798` n `20`; unknown avg `0.0585` n `748`
- 4h: commodity avg `-0.1559` n `12`; crypto_alt avg `0.6249` n `229`; crypto_major avg `0.6358` n `8`; equity avg `-0.058` n `91`; fx avg `-0.001` n `6`; index avg `0.0255` n `25`; metal avg `0.148` n `20`; unknown avg `0.0055` n `748`
- 24h: commodity avg `0.003` n `12`; crypto_alt avg `0.4838` n `229`; crypto_major avg `0.1043` n `8`; equity avg `1.2382` n `91`; fx avg `0.0686` n `6`; index avg `0.0899` n `25`; metal avg `-0.7553` n `20`; unknown avg `0.0718` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.0998`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0694`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0651`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0631`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0628`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0593`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0583`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0548`, n `669`, weak_sample_signal
