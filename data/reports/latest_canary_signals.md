# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T14:22:25.915021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1408` n `12`; crypto_alt avg `-0.5174` n `228`; crypto_major avg `-0.3911` n `8`; equity avg `-0.2265` n `67`; fx avg `0.04` n `6`; index avg `-0.1892` n `23`; metal avg `0.1136` n `18`; unknown avg `0.5617` n `418`
- 1h: commodity avg `0.1402` n `12`; crypto_alt avg `-0.4964` n `228`; crypto_major avg `-0.767` n `8`; equity avg `-0.4822` n `67`; fx avg `0.0111` n `6`; index avg `-0.6297` n `23`; metal avg `0.4399` n `18`; unknown avg `-0.3489` n `418`
- 4h: commodity avg `0.194` n `12`; crypto_alt avg `-0.5536` n `228`; crypto_major avg `-1.2575` n `8`; equity avg `-0.8391` n `67`; fx avg `0.0255` n `6`; index avg `-0.7684` n `23`; metal avg `-0.4532` n `18`; unknown avg `0.3806` n `418`
- 24h: commodity avg `-1.6219` n `12`; crypto_alt avg `-3.3127` n `228`; crypto_major avg `-3.026` n `8`; equity avg `-0.3804` n `67`; fx avg `-0.0166` n `6`; index avg `-0.5361` n `23`; metal avg `-1.0212` n `18`; unknown avg `0.3755` n `398`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1756`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
