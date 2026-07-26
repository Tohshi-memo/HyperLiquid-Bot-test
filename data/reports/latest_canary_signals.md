# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T07:52:28.801342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `-0.0818` n `230`; crypto_major avg `-0.0652` n `8`; equity avg `-0.0111` n `100`; fx avg `0.0042` n `6`; index avg `0.0022` n `25`; metal avg `0.006` n `20`; unknown avg `-0.0098` n `775`
- 1h: commodity avg `-0.1287` n `12`; crypto_alt avg `0.0881` n `230`; crypto_major avg `-0.1031` n `8`; equity avg `-0.0406` n `100`; fx avg `-0.003` n `6`; index avg `0.0045` n `25`; metal avg `0.0214` n `20`; unknown avg `-0.0254` n `775`
- 4h: commodity avg `-0.0588` n `12`; crypto_alt avg `0.4029` n `230`; crypto_major avg `0.0374` n `8`; equity avg `-0.0034` n `100`; fx avg `0.0624` n `6`; index avg `-0.0012` n `25`; metal avg `0.024` n `20`; unknown avg `-0.009` n `759`
- 24h: commodity avg `-0.5849` n `12`; crypto_alt avg `1.6195` n `230`; crypto_major avg `1.6989` n `8`; equity avg `0.5061` n `100`; fx avg `0.0408` n `6`; index avg `0.1352` n `25`; metal avg `0.06` n `20`; unknown avg `0.0098` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1862`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1416`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1273`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1237`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1203`, n `666`, weak_sample_signal
