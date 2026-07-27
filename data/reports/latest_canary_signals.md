# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T07:22:28.608518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0545` n `12`; crypto_alt avg `0.1255` n `230`; crypto_major avg `0.0139` n `8`; equity avg `0.0171` n `100`; fx avg `-0.0241` n `6`; index avg `0.0031` n `25`; metal avg `0.0864` n `20`; unknown avg `0.1264` n `775`
- 1h: commodity avg `-0.1059` n `12`; crypto_alt avg `-0.0066` n `230`; crypto_major avg `-0.0136` n `8`; equity avg `0.1678` n `100`; fx avg `-0.0134` n `6`; index avg `-0.0008` n `25`; metal avg `0.1746` n `20`; unknown avg `0.106` n `775`
- 4h: commodity avg `-0.4309` n `12`; crypto_alt avg `0.1089` n `230`; crypto_major avg `0.495` n `8`; equity avg `0.639` n `100`; fx avg `0.0054` n `6`; index avg `0.083` n `25`; metal avg `0.2412` n `20`; unknown avg `0.1037` n `759`
- 24h: commodity avg `-0.7991` n `12`; crypto_alt avg `0.9368` n `230`; crypto_major avg `1.4753` n `8`; equity avg `1.4273` n `100`; fx avg `0.0784` n `6`; index avg `0.1867` n `25`; metal avg `0.5715` n `20`; unknown avg `0.0564` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
