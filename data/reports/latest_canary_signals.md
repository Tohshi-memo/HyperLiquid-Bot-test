# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T12:52:33.311753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `12`; crypto_alt avg `-0.2828` n `230`; crypto_major avg `-0.2262` n `8`; equity avg `-0.1717` n `100`; fx avg `0.0068` n `6`; index avg `-0.0402` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0541` n `773`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.2` n `230`; crypto_major avg `-0.1796` n `8`; equity avg `0.0227` n `100`; fx avg `-0.006` n `6`; index avg `0.008` n `25`; metal avg `0.0337` n `20`; unknown avg `-0.0587` n `773`
- 4h: commodity avg `0.1718` n `12`; crypto_alt avg `-0.7713` n `230`; crypto_major avg `-0.7718` n `8`; equity avg `0.066` n `100`; fx avg `-0.0393` n `6`; index avg `0.0109` n `25`; metal avg `0.0642` n `20`; unknown avg `-0.0127` n `773`
- 24h: commodity avg `-0.3074` n `12`; crypto_alt avg `-1.3902` n `230`; crypto_major avg `-1.4809` n `8`; equity avg `-0.5926` n `100`; fx avg `-0.1645` n `6`; index avg `-0.2072` n `25`; metal avg `-0.0856` n `20`; unknown avg `0.1592` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0826`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0824`, n `666`, weak_sample_signal
