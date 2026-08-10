# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T07:37:24.604424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0432` n `12`; crypto_alt avg `0.0444` n `230`; crypto_major avg `0.0796` n `8`; equity avg `0.0746` n `112`; fx avg `0.0133` n `6`; index avg `0.0073` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0122` n `785`
- 1h: commodity avg `0.079` n `12`; crypto_alt avg `0.1198` n `230`; crypto_major avg `0.2881` n `8`; equity avg `0.1794` n `112`; fx avg `0.0078` n `6`; index avg `0.0242` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0554` n `785`
- 4h: commodity avg `-0.0689` n `12`; crypto_alt avg `0.273` n `230`; crypto_major avg `0.3951` n `8`; equity avg `0.2572` n `112`; fx avg `0.105` n `6`; index avg `0.0402` n `25`; metal avg `0.1243` n `20`; unknown avg `57.187` n `753`
- 24h: commodity avg `0.3304` n `12`; crypto_alt avg `0.9994` n `230`; crypto_major avg `0.3585` n `8`; equity avg `-0.0285` n `112`; fx avg `0.2044` n `6`; index avg `0.0689` n `25`; metal avg `-0.0242` n `20`; unknown avg `56.9248` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1897`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1443`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1353`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.111`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0967`, n `669`, weak_sample_signal
