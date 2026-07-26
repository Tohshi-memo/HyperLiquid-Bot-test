# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T06:22:28.884516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1019` n `12`; crypto_alt avg `-0.2227` n `230`; crypto_major avg `-0.2375` n `8`; equity avg `-0.0137` n `100`; fx avg `0.0005` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.0167` n `775`
- 1h: commodity avg `0.1215` n `12`; crypto_alt avg `-0.1723` n `230`; crypto_major avg `-0.3707` n `8`; equity avg `-0.0509` n `100`; fx avg `0.0006` n `6`; index avg `-0.008` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.024` n `759`
- 4h: commodity avg `0.005` n `12`; crypto_alt avg `0.2356` n `230`; crypto_major avg `-0.0449` n `8`; equity avg `0.0057` n `100`; fx avg `0.0679` n `6`; index avg `-0.0001` n `25`; metal avg `0.0081` n `20`; unknown avg `-0.0024` n `758`
- 24h: commodity avg `-0.4391` n `12`; crypto_alt avg `1.1203` n `230`; crypto_major avg `1.4032` n `8`; equity avg `0.4101` n `100`; fx avg `0.0678` n `6`; index avg `0.1149` n `25`; metal avg `0.0528` n `20`; unknown avg `-0.1352` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1382`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1229`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1203`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
