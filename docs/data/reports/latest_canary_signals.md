# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T00:52:29.942524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.0896` n `228`; crypto_major avg `0.0515` n `8`; equity avg `0.0113` n `78`; fx avg `0.0005` n `6`; index avg `0.0007` n `23`; metal avg `-0.0033` n `18`; unknown avg `0.1433` n `701`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `0.1599` n `228`; crypto_major avg `-0.1146` n `8`; equity avg `-0.0074` n `78`; fx avg `-0.0016` n `6`; index avg `-0.0104` n `23`; metal avg `-0.0266` n `18`; unknown avg `0.0179` n `701`
- 4h: commodity avg `0.1038` n `12`; crypto_alt avg `0.8481` n `228`; crypto_major avg `0.5613` n `8`; equity avg `0.0978` n `78`; fx avg `0.0003` n `6`; index avg `0.0066` n `23`; metal avg `-0.0072` n `18`; unknown avg `0.2425` n `701`
- 24h: commodity avg `0.4232` n `12`; crypto_alt avg `1.0478` n `228`; crypto_major avg `1.505` n `8`; equity avg `0.3849` n `78`; fx avg `0.0574` n `6`; index avg `0.0083` n `23`; metal avg `-0.0863` n `18`; unknown avg `-0.2105` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
