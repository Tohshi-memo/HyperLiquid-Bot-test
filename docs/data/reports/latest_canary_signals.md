# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T13:22:20.240899+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `77.66` - News risk is high; compare crypto drawdown vs metal/index behavior.
- 4h_commodity_crypto_divergence: score `-2.3664` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8502` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7246` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.0169` n `228`; crypto_major avg `0.0531` n `8`; equity avg `-0.0964` n `74`; fx avg `0.0013` n `6`; index avg `-0.011` n `23`; metal avg `0.0056` n `18`; unknown avg `0.0208` n `516`
- 1h: commodity avg `0.0824` n `12`; crypto_alt avg `0.1632` n `228`; crypto_major avg `0.1029` n `8`; equity avg `-0.1307` n `74`; fx avg `0.0105` n `6`; index avg `-0.0407` n `23`; metal avg `-0.0871` n `18`; unknown avg `0.1975` n `516`
- 4h: commodity avg `0.29` n `12`; crypto_alt avg `-2.0143` n `228`; crypto_major avg `-2.0764` n `8`; equity avg `-0.5978` n `74`; fx avg `0.0091` n `6`; index avg `-0.2262` n `23`; metal avg `-0.3518` n `18`; unknown avg `-3.4002` n `516`
- 24h: commodity avg `0.2139` n `12`; crypto_alt avg `1.1996` n `228`; crypto_major avg `1.3287` n `8`; equity avg `1.0452` n `74`; fx avg `0.0253` n `6`; index avg `0.2604` n `23`; metal avg `0.3136` n `18`; unknown avg `-0.3783` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1309`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
