# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T02:22:18.289872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `-0.1203` n `228`; crypto_major avg `0.0107` n `8`; equity avg `-0.0333` n `67`; fx avg `0.0012` n `6`; index avg `-0.0472` n `23`; metal avg `-0.021` n `18`; unknown avg `-0.0253` n `396`
- 1h: commodity avg `0.064` n `12`; crypto_alt avg `-0.2646` n `228`; crypto_major avg `-0.1637` n `8`; equity avg `0.0164` n `67`; fx avg `-0.013` n `6`; index avg `0.0155` n `23`; metal avg `0.0198` n `18`; unknown avg `-0.3419` n `396`
- 4h: commodity avg `0.2179` n `12`; crypto_alt avg `-0.3814` n `228`; crypto_major avg `0.5577` n `8`; equity avg `0.3371` n `67`; fx avg `-0.0159` n `6`; index avg `0.3076` n `23`; metal avg `0.4843` n `18`; unknown avg `0.237` n `396`
- 24h: commodity avg `-2.9129` n `12`; crypto_alt avg `2.0504` n `228`; crypto_major avg `2.6289` n `8`; equity avg `2.2333` n `67`; fx avg `0.044` n `6`; index avg `1.1325` n `23`; metal avg `1.1837` n `18`; unknown avg `1.6523` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
