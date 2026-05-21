# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T16:37:19.828127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.12` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0683` n `12`; crypto_alt avg `-0.0287` n `228`; crypto_major avg `-0.1829` n `8`; equity avg `0.0111` n `67`; fx avg `0.0024` n `6`; index avg `-0.0176` n `23`; metal avg `-0.0026` n `18`; unknown avg `-0.2971` n `385`
- 1h: commodity avg `-0.4032` n `12`; crypto_alt avg `-0.1453` n `228`; crypto_major avg `-0.4729` n `8`; equity avg `0.2186` n `67`; fx avg `0.0232` n `6`; index avg `0.0864` n `23`; metal avg `0.3737` n `18`; unknown avg `-0.4942` n `385`
- 4h: commodity avg `0.0406` n `12`; crypto_alt avg `0.6909` n `228`; crypto_major avg `0.5222` n `8`; equity avg `0.5078` n `67`; fx avg `-0.029` n `6`; index avg `0.0157` n `23`; metal avg `0.7612` n `18`; unknown avg `0.961` n `385`
- 24h: commodity avg `0.4251` n `12`; crypto_alt avg `1.1725` n `228`; crypto_major avg `1.8951` n `8`; equity avg `1.0913` n `66`; fx avg `0.0016` n `6`; index avg `0.1947` n `23`; metal avg `0.0596` n `18`; unknown avg `7.0081` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0453`, n `668`, weak_sample_signal
