# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T14:52:27.405868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `75.57` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0442` n `12`; crypto_alt avg `-0.3482` n `228`; crypto_major avg `-0.4075` n `8`; equity avg `-0.212` n `74`; fx avg `0.0013` n `6`; index avg `0.0402` n `23`; metal avg `-0.0714` n `18`; unknown avg `-0.0927` n `516`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `0.706` n `228`; crypto_major avg `0.6096` n `8`; equity avg `0.2396` n `74`; fx avg `-0.0081` n `6`; index avg `0.1943` n `23`; metal avg `-0.0177` n `18`; unknown avg `0.1549` n `516`
- 4h: commodity avg `0.199` n `12`; crypto_alt avg `0.2707` n `228`; crypto_major avg `-0.0836` n `8`; equity avg `0.4989` n `74`; fx avg `0.0191` n `6`; index avg `0.328` n `23`; metal avg `-0.1472` n `18`; unknown avg `0.1879` n `516`
- 24h: commodity avg `0.0632` n `12`; crypto_alt avg `2.1094` n `228`; crypto_major avg `1.9845` n `8`; equity avg `1.6569` n `74`; fx avg `0.0183` n `6`; index avg `0.5262` n `23`; metal avg `0.6082` n `18`; unknown avg `-4.3061` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
