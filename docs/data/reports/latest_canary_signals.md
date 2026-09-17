# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T22:37:24.230717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0143` n `12`; crypto_alt avg `0.297` n `234`; crypto_major avg `0.3265` n `8`; equity avg `-0.012` n `140`; fx avg `0.0031` n `6`; index avg `0.0011` n `26`; metal avg `0.019` n `20`; unknown avg `0.2214` n `895`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `-0.1003` n `234`; crypto_major avg `-0.0004` n `8`; equity avg `-0.1054` n `140`; fx avg `0.0137` n `6`; index avg `-0.0226` n `26`; metal avg `0.03` n `20`; unknown avg `0.6125` n `853`
- 4h: commodity avg `-0.1686` n `12`; crypto_alt avg `0.1231` n `234`; crypto_major avg `0.3372` n `8`; equity avg `-0.0019` n `140`; fx avg `-0.0069` n `6`; index avg `-0.0289` n `26`; metal avg `-0.0481` n `20`; unknown avg `0.3481` n `793`
- 24h: commodity avg `-0.1734` n `12`; crypto_alt avg `4.1753` n `234`; crypto_major avg `2.3872` n `8`; equity avg `1.9904` n `138`; fx avg `0.0005` n `6`; index avg `0.3583` n `26`; metal avg `0.5441` n `20`; unknown avg `2.4854` n `759`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
