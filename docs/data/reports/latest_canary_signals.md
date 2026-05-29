# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T02:07:21.787918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1719` n `12`; crypto_alt avg `0.1215` n `228`; crypto_major avg `0.0873` n `8`; equity avg `0.0263` n `69`; fx avg `-0.0082` n `6`; index avg `0.001` n `23`; metal avg `-0.0333` n `18`; unknown avg `0.2243` n `417`
- 1h: commodity avg `-0.1398` n `12`; crypto_alt avg `-0.2598` n `228`; crypto_major avg `-0.3422` n `8`; equity avg `-0.0498` n `69`; fx avg `-0.0253` n `6`; index avg `0.0137` n `23`; metal avg `0.005` n `18`; unknown avg `-0.1149` n `417`
- 4h: commodity avg `-0.2847` n `12`; crypto_alt avg `0.1314` n `228`; crypto_major avg `-0.305` n `8`; equity avg `0.0579` n `69`; fx avg `0.0705` n `6`; index avg `-0.1108` n `23`; metal avg `0.0879` n `18`; unknown avg `-0.3334` n `417`
- 24h: commodity avg `0.3772` n `12`; crypto_alt avg `-1.1382` n `228`; crypto_major avg `0.4649` n `8`; equity avg `2.5706` n `69`; fx avg `0.0506` n `6`; index avg `0.8045` n `23`; metal avg `1.8153` n `18`; unknown avg `0.3109` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
