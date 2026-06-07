# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T15:07:22.186775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0514` n `12`; crypto_alt avg `-0.1778` n `228`; crypto_major avg `-0.2976` n `8`; equity avg `-0.0195` n `74`; fx avg `-0.0001` n `6`; index avg `-0.2118` n `23`; metal avg `0.0006` n `18`; unknown avg `0.0242` n `516`
- 1h: commodity avg `0.1437` n `12`; crypto_alt avg `0.4809` n `228`; crypto_major avg `0.1495` n `8`; equity avg `0.1136` n `74`; fx avg `-0.0029` n `6`; index avg `-0.0824` n `23`; metal avg `-0.0329` n `18`; unknown avg `0.1762` n `516`
- 4h: commodity avg `0.2553` n `12`; crypto_alt avg `0.1103` n `228`; crypto_major avg `-0.3368` n `8`; equity avg `0.4451` n `74`; fx avg `0.0034` n `6`; index avg `0.1122` n `23`; metal avg `-0.1438` n `18`; unknown avg `0.1491` n `516`
- 24h: commodity avg `0.1958` n `12`; crypto_alt avg `2.7183` n `228`; crypto_major avg `2.6608` n `8`; equity avg `1.8067` n `74`; fx avg `0.023` n `6`; index avg `0.3665` n `23`; metal avg `0.6249` n `18`; unknown avg `-5.1015` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
