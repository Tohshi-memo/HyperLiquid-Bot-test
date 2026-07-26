# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T10:37:26.562179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `0.0609` n `230`; crypto_major avg `0.0651` n `8`; equity avg `0.0623` n `100`; fx avg `0.0015` n `6`; index avg `0.012` n `25`; metal avg `0.0253` n `20`; unknown avg `0.0558` n `775`
- 1h: commodity avg `-0.2373` n `12`; crypto_alt avg `0.098` n `230`; crypto_major avg `0.1189` n `8`; equity avg `0.1537` n `100`; fx avg `0.0041` n `6`; index avg `0.0476` n `25`; metal avg `0.0563` n `20`; unknown avg `0.0398` n `775`
- 4h: commodity avg `-0.3553` n `12`; crypto_alt avg `0.2895` n `230`; crypto_major avg `0.27` n `8`; equity avg `0.2071` n `100`; fx avg `-0.0394` n `6`; index avg `0.0677` n `25`; metal avg `0.1169` n `20`; unknown avg `-0.0487` n `775`
- 24h: commodity avg `-0.8919` n `12`; crypto_alt avg `1.6978` n `230`; crypto_major avg `1.7721` n `8`; equity avg `0.7351` n `100`; fx avg `0.0058` n `6`; index avg `0.182` n `25`; metal avg `0.159` n `20`; unknown avg `0.1074` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1863`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1455`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.135`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1302`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1246`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
