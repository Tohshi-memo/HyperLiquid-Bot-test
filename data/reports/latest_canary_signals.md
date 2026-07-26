# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T18:07:26.700023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `-0.0786` n `230`; crypto_major avg `-0.0494` n `8`; equity avg `0.0251` n `100`; fx avg `0.0153` n `6`; index avg `-0.0065` n `25`; metal avg `0.0212` n `20`; unknown avg `0.0003` n `775`
- 1h: commodity avg `0.0184` n `12`; crypto_alt avg `-0.1161` n `230`; crypto_major avg `-0.1483` n `8`; equity avg `-0.0018` n `100`; fx avg `0.0148` n `6`; index avg `0.0014` n `25`; metal avg `0.0076` n `20`; unknown avg `1.076` n `775`
- 4h: commodity avg `-0.0383` n `12`; crypto_alt avg `0.1717` n `230`; crypto_major avg `0.1558` n `8`; equity avg `0.0699` n `100`; fx avg `-0.0034` n `6`; index avg `0.0121` n `25`; metal avg `0.0092` n `20`; unknown avg `-0.0788` n `775`
- 24h: commodity avg `-0.3308` n `12`; crypto_alt avg `0.6085` n `230`; crypto_major avg `0.5692` n `8`; equity avg `0.7266` n `100`; fx avg `0.0455` n `6`; index avg `0.1438` n `25`; metal avg `0.1912` n `20`; unknown avg `0.0498` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1938`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1839`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1653`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.148`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1399`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1325`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1313`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1311`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.13`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1292`, n `669`, weak_sample_signal
