# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T16:37:31.015757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0785` n `12`; crypto_alt avg `-0.1765` n `230`; crypto_major avg `-0.2412` n `8`; equity avg `-0.3983` n `100`; fx avg `-0.0072` n `6`; index avg `-0.0728` n `25`; metal avg `-0.0607` n `20`; unknown avg `0.0613` n `773`
- 1h: commodity avg `-0.058` n `12`; crypto_alt avg `-0.2304` n `230`; crypto_major avg `-0.3309` n `8`; equity avg `0.089` n `100`; fx avg `-0.0186` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0246` n `773`
- 4h: commodity avg `-0.2719` n `12`; crypto_alt avg `-0.9218` n `230`; crypto_major avg `-0.9111` n `8`; equity avg `-1.8673` n `100`; fx avg `0.0308` n `6`; index avg `-0.1269` n `25`; metal avg `0.0445` n `20`; unknown avg `13.3109` n `773`
- 24h: commodity avg `-0.6837` n `12`; crypto_alt avg `-1.5233` n `230`; crypto_major avg `-1.2036` n `8`; equity avg `-2.4825` n `100`; fx avg `-0.1214` n `6`; index avg `-0.2621` n `25`; metal avg `0.1524` n `20`; unknown avg `13.6454` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1438`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1188`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1124`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1112`, n `667`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1032`, n `667`, weak_sample_signal
