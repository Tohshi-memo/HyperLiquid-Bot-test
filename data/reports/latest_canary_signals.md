# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T20:52:19.696754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2305` n `12`; crypto_alt avg `0.1616` n `228`; crypto_major avg `0.0592` n `8`; equity avg `0.1327` n `66`; fx avg `-0.0053` n `6`; index avg `-0.0265` n `23`; metal avg `-0.0495` n `18`; unknown avg `0.0792` n `384`
- 1h: commodity avg `0.2479` n `12`; crypto_alt avg `-0.0384` n `228`; crypto_major avg `-0.1652` n `8`; equity avg `0.0461` n `66`; fx avg `-0.0704` n `6`; index avg `-0.0542` n `23`; metal avg `-0.1875` n `18`; unknown avg `-0.106` n `384`
- 4h: commodity avg `0.4738` n `12`; crypto_alt avg `0.3183` n `228`; crypto_major avg `0.109` n `8`; equity avg `0.244` n `66`; fx avg `-0.0458` n `6`; index avg `0.1637` n `23`; metal avg `0.1001` n `18`; unknown avg `0.3178` n `384`
- 24h: commodity avg `-2.2516` n `12`; crypto_alt avg `2.7495` n `228`; crypto_major avg `1.8323` n `8`; equity avg `1.7351` n `66`; fx avg `-0.0866` n `6`; index avg `1.2005` n `23`; metal avg `1.5641` n `18`; unknown avg `0.9206` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0454`, n `668`, weak_sample_signal
