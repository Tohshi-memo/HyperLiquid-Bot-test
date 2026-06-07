# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T13:37:23.979701+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `76.46` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_index_leads_crypto: score `1.4343` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0397` n `12`; crypto_alt avg `0.08` n `228`; crypto_major avg `-0.0792` n `8`; equity avg `0.1425` n `74`; fx avg `0.0129` n `6`; index avg `0.0086` n `23`; metal avg `0.0074` n `18`; unknown avg `0.0139` n `516`
- 1h: commodity avg `0.0615` n `12`; crypto_alt avg `0.3267` n `228`; crypto_major avg `0.0032` n `8`; equity avg `0.0569` n `74`; fx avg `0.015` n `6`; index avg `0.0127` n `23`; metal avg `-0.0002` n `18`; unknown avg `0.2415` n `516`
- 4h: commodity avg `0.2216` n `12`; crypto_alt avg `-1.3515` n `228`; crypto_major avg `-1.5513` n `8`; equity avg `-0.29` n `74`; fx avg `0.0249` n `6`; index avg `-0.117` n `23`; metal avg `-0.3252` n `18`; unknown avg `-3.2405` n `516`
- 24h: commodity avg `0.1966` n `12`; crypto_alt avg `1.5055` n `228`; crypto_major avg `1.585` n `8`; equity avg `1.3767` n `74`; fx avg `0.0375` n `6`; index avg `0.3031` n `23`; metal avg `0.3402` n `18`; unknown avg `1.7845` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
