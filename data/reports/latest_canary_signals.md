# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T04:07:30.199059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0749` n `12`; crypto_alt avg `0.134` n `230`; crypto_major avg `0.1469` n `8`; equity avg `0.0387` n `100`; fx avg `0.0072` n `6`; index avg `0.0143` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.1865` n `775`
- 1h: commodity avg `-0.0795` n `12`; crypto_alt avg `0.0963` n `230`; crypto_major avg `0.3185` n `8`; equity avg `0.0231` n `100`; fx avg `-0.0025` n `6`; index avg `-0.0118` n `25`; metal avg `-0.0037` n `20`; unknown avg `-0.3385` n `775`
- 4h: commodity avg `-0.0429` n `12`; crypto_alt avg `0.0996` n `230`; crypto_major avg `0.0567` n `8`; equity avg `0.1019` n `100`; fx avg `0.0839` n `6`; index avg `-0.0507` n `25`; metal avg `-0.1057` n `20`; unknown avg `-0.3974` n `775`
- 24h: commodity avg `-0.5386` n `12`; crypto_alt avg `1.3509` n `230`; crypto_major avg `1.4263` n `8`; equity avg `0.706` n `100`; fx avg `0.0981` n `6`; index avg `0.0412` n `25`; metal avg `0.321` n `20`; unknown avg `-0.0181` n `759`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
