# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T00:37:27.702126+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.3009` n `234`; crypto_major avg `0.1833` n `8`; equity avg `0.0003` n `140`; fx avg `0.0087` n `6`; index avg `0.014` n `26`; metal avg `0.0427` n `20`; unknown avg `-0.1753` n `913`
- 1h: commodity avg `-0.0528` n `12`; crypto_alt avg `0.1842` n `234`; crypto_major avg `0.0628` n `8`; equity avg `-0.1067` n `140`; fx avg `0.053` n `6`; index avg `-0.0524` n `26`; metal avg `0.0954` n `20`; unknown avg `-0.0532` n `911`
- 4h: commodity avg `-0.0959` n `12`; crypto_alt avg `0.5688` n `234`; crypto_major avg `0.2143` n `8`; equity avg `-0.1353` n `140`; fx avg `0.0641` n `6`; index avg `-0.0659` n `26`; metal avg `0.1445` n `20`; unknown avg `-0.0478` n `815`
- 24h: commodity avg `-0.146` n `12`; crypto_alt avg `3.4202` n `234`; crypto_major avg `1.9208` n `8`; equity avg `1.4767` n `138`; fx avg `0.0777` n `6`; index avg `0.2177` n `26`; metal avg `0.5525` n `20`; unknown avg `1.7159` n `765`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
