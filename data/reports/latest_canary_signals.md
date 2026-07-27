# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T10:07:30.801010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0809` n `12`; crypto_alt avg `-0.0251` n `230`; crypto_major avg `-0.0704` n `8`; equity avg `-0.0125` n `100`; fx avg `0.0004` n `6`; index avg `-0.0136` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.0406` n `775`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.2284` n `230`; crypto_major avg `0.15` n `8`; equity avg `0.177` n `100`; fx avg `-0.0144` n `6`; index avg `0.0182` n `25`; metal avg `-0.0164` n `20`; unknown avg `0.0393` n `775`
- 4h: commodity avg `-0.4367` n `12`; crypto_alt avg `-0.6452` n `230`; crypto_major avg `-0.4732` n `8`; equity avg `0.4304` n `100`; fx avg `-0.0086` n `6`; index avg `0.0299` n `25`; metal avg `0.0844` n `20`; unknown avg `-0.0889` n `775`
- 24h: commodity avg `-0.6994` n `12`; crypto_alt avg `0.5834` n `230`; crypto_major avg `1.1893` n `8`; equity avg `1.5359` n `100`; fx avg `0.1067` n `6`; index avg `0.1894` n `25`; metal avg `0.4259` n `20`; unknown avg `-0.0705` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1964`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
