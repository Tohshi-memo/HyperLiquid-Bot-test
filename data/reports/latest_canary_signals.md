# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T08:22:32.287315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `0.0485` n `230`; crypto_major avg `0.0384` n `8`; equity avg `-0.015` n `100`; fx avg `-0.0012` n `6`; index avg `0.005` n `25`; metal avg `0.0101` n `20`; unknown avg `-0.0032` n `775`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `0.0642` n `230`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0254` n `100`; fx avg `-0.036` n `6`; index avg `0.0028` n `25`; metal avg `0.0272` n `20`; unknown avg `0.0297` n `775`
- 4h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.5037` n `230`; crypto_major avg `0.0731` n `8`; equity avg `-0.0477` n `100`; fx avg `-0.0412` n `6`; index avg `-0.0046` n `25`; metal avg `0.0312` n `20`; unknown avg `0.0289` n `759`
- 24h: commodity avg `-0.6093` n `12`; crypto_alt avg `1.7637` n `230`; crypto_major avg `1.7145` n `8`; equity avg `0.5096` n `100`; fx avg `0.0034` n `6`; index avg `0.1441` n `25`; metal avg `0.0863` n `20`; unknown avg `0.0383` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1731`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1433`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1283`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1255`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1209`, n `666`, weak_sample_signal
