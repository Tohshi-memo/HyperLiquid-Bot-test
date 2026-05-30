# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T14:52:19.454695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.2264` n `228`; crypto_major avg `-0.1213` n `8`; equity avg `0.0228` n `69`; fx avg `0.003` n `6`; index avg `0.0096` n `23`; metal avg `-0.0166` n `18`; unknown avg `-0.0189` n `421`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.1563` n `228`; crypto_major avg `0.3833` n `8`; equity avg `0.1134` n `69`; fx avg `0.0219` n `6`; index avg `0.1213` n `23`; metal avg `0.0017` n `18`; unknown avg `0.2777` n `421`
- 4h: commodity avg `0.2455` n `12`; crypto_alt avg `0.0389` n `228`; crypto_major avg `0.5486` n `8`; equity avg `0.3666` n `69`; fx avg `0.0227` n `6`; index avg `0.1851` n `23`; metal avg `-0.0516` n `18`; unknown avg `0.0653` n `421`
- 24h: commodity avg `0.0189` n `12`; crypto_alt avg `2.3006` n `228`; crypto_major avg `3.1377` n `8`; equity avg `2.008` n `69`; fx avg `0.0677` n `6`; index avg `0.441` n `23`; metal avg `-0.297` n `18`; unknown avg `0.7503` n `400`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1919`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
