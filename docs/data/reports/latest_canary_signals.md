# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T04:22:19.534671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0806` n `12`; crypto_alt avg `-0.3634` n `228`; crypto_major avg `-0.2936` n `8`; equity avg `-0.0371` n `69`; fx avg `0.0` n `6`; index avg `-0.0146` n `23`; metal avg `-0.0109` n `18`; unknown avg `0.0372` n `419`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `-0.7264` n `228`; crypto_major avg `-0.5068` n `8`; equity avg `-0.1183` n `69`; fx avg `0.0` n `6`; index avg `-0.0088` n `23`; metal avg `-0.0669` n `18`; unknown avg `0.7316` n `419`
- 4h: commodity avg `-0.1601` n `12`; crypto_alt avg `0.5428` n `228`; crypto_major avg `0.5095` n `8`; equity avg `0.2334` n `69`; fx avg `0.0028` n `6`; index avg `-0.0822` n `23`; metal avg `-0.0597` n `18`; unknown avg `0.3859` n `419`
- 24h: commodity avg `-0.0984` n `12`; crypto_alt avg `1.9031` n `228`; crypto_major avg `2.0177` n `8`; equity avg `0.9198` n `69`; fx avg `0.114` n `6`; index avg `0.0515` n `23`; metal avg `-0.0213` n `18`; unknown avg `1.6808` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
