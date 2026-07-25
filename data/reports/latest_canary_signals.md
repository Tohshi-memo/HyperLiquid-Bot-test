# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T23:52:29.254671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.0476` n `230`; crypto_major avg `-0.0397` n `8`; equity avg `0.0158` n `100`; fx avg `0.0093` n `6`; index avg `0.0086` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.0271` n `774`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `-0.2131` n `230`; crypto_major avg `-0.1238` n `8`; equity avg `0.0547` n `100`; fx avg `0.0146` n `6`; index avg `0.0083` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.0742` n `774`
- 4h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.1827` n `230`; crypto_major avg `-0.235` n `8`; equity avg `0.1131` n `100`; fx avg `0.0108` n `6`; index avg `0.0295` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.176` n `774`
- 24h: commodity avg `-0.6195` n `12`; crypto_alt avg `0.3873` n `230`; crypto_major avg `0.9189` n `8`; equity avg `0.6344` n `100`; fx avg `-0.0229` n `6`; index avg `0.1793` n `25`; metal avg `-0.0027` n `20`; unknown avg `-0.2732` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1349`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1232`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1163`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
