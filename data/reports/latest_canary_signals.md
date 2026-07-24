# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T03:37:25.429568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0478` n `12`; crypto_alt avg `0.0005` n `230`; crypto_major avg `-0.0134` n `8`; equity avg `-0.096` n `100`; fx avg `0.0117` n `6`; index avg `-0.0006` n `25`; metal avg `0.0182` n `20`; unknown avg `0.4805` n `772`
- 1h: commodity avg `0.0978` n `12`; crypto_alt avg `0.4192` n `230`; crypto_major avg `0.4847` n `8`; equity avg `-0.1917` n `100`; fx avg `0.0157` n `6`; index avg `-0.0371` n `25`; metal avg `-0.0346` n `20`; unknown avg `0.6985` n `772`
- 4h: commodity avg `0.0436` n `12`; crypto_alt avg `0.3201` n `230`; crypto_major avg `0.1269` n `8`; equity avg `-0.8274` n `100`; fx avg `-0.0972` n `6`; index avg `-0.2738` n `25`; metal avg `-0.1737` n `20`; unknown avg `-0.2674` n `772`
- 24h: commodity avg `0.579` n `12`; crypto_alt avg `-0.8338` n `230`; crypto_major avg `-1.6663` n `8`; equity avg `-2.0899` n `99`; fx avg `-0.1131` n `6`; index avg `-0.5444` n `25`; metal avg `-1.0506` n `20`; unknown avg `-0.2879` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1822`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1121`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1023`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
