# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T18:22:23.008488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0732` n `12`; crypto_alt avg `-0.1522` n `228`; crypto_major avg `-0.0422` n `8`; equity avg `-0.1117` n `74`; fx avg `-0.0078` n `6`; index avg `-0.0846` n `23`; metal avg `-0.0203` n `18`; unknown avg `0.1235` n `516`
- 1h: commodity avg `0.0871` n `12`; crypto_alt avg `-0.3132` n `228`; crypto_major avg `-0.0699` n `8`; equity avg `-0.2807` n `74`; fx avg `-0.0079` n `6`; index avg `-0.1577` n `23`; metal avg `-0.0613` n `18`; unknown avg `0.1368` n `516`
- 4h: commodity avg `0.2949` n `12`; crypto_alt avg `0.0387` n `228`; crypto_major avg `0.5848` n `8`; equity avg `-0.1294` n `74`; fx avg `-0.0096` n `6`; index avg `-0.194` n `23`; metal avg `0.0269` n `18`; unknown avg `-2.1678` n `516`
- 24h: commodity avg `0.2919` n `12`; crypto_alt avg `3.2043` n `228`; crypto_major avg `3.9329` n `8`; equity avg `1.8738` n `74`; fx avg `-0.2134` n `6`; index avg `0.3087` n `23`; metal avg `0.6266` n `18`; unknown avg `-4.6752` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
