# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T05:22:31.778646+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0207` n `12`; crypto_alt avg `-0.0922` n `230`; crypto_major avg `-0.0396` n `8`; equity avg `-0.0205` n `100`; fx avg `-0.001` n `6`; index avg `-0.0059` n `25`; metal avg `0.002` n `20`; unknown avg `0.0601` n `774`
- 1h: commodity avg `0.0065` n `12`; crypto_alt avg `-0.103` n `230`; crypto_major avg `-0.0006` n `8`; equity avg `-0.0682` n `100`; fx avg `-0.003` n `6`; index avg `0.0045` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.3979` n `774`
- 4h: commodity avg `-0.1575` n `12`; crypto_alt avg `-0.0179` n `230`; crypto_major avg `0.1754` n `8`; equity avg `0.2066` n `100`; fx avg `-0.0368` n `6`; index avg `0.0459` n `25`; metal avg `-0.0081` n `20`; unknown avg `0.0777` n `774`
- 24h: commodity avg `-0.4522` n `12`; crypto_alt avg `-1.2315` n `230`; crypto_major avg `-0.9689` n `8`; equity avg `-2.583` n `100`; fx avg `-0.0469` n `6`; index avg `-0.1995` n `25`; metal avg `0.1538` n `20`; unknown avg `13.6782` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1147`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1039`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1006`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0993`, n `666`, weak_sample_signal
