# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T08:37:30.644852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0493` n `228`; crypto_major avg `-0.0728` n `8`; equity avg `-0.0168` n `78`; fx avg `-0.0038` n `6`; index avg `0.0197` n `23`; metal avg `0.0032` n `18`; unknown avg `-0.0129` n `687`
- 1h: commodity avg `-0.0171` n `12`; crypto_alt avg `-0.1403` n `228`; crypto_major avg `-0.2831` n `8`; equity avg `0.0235` n `78`; fx avg `0.2955` n `6`; index avg `0.0166` n `23`; metal avg `-0.013` n `18`; unknown avg `-0.0466` n `687`
- 4h: commodity avg `0.106` n `12`; crypto_alt avg `0.3636` n `228`; crypto_major avg `0.6498` n `8`; equity avg `0.1999` n `78`; fx avg `0.0014` n `6`; index avg `-0.0071` n `23`; metal avg `0.0264` n `18`; unknown avg `-0.0107` n `639`
- 24h: commodity avg `0.5241` n `12`; crypto_alt avg `-3.2244` n `228`; crypto_major avg `-3.5778` n `8`; equity avg `1.3195` n `78`; fx avg `-0.0998` n `6`; index avg `0.3067` n `23`; metal avg `-4.0954` n `18`; unknown avg `0.0473` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
