# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T01:52:30.408734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0302` n `12`; crypto_alt avg `-0.0295` n `230`; crypto_major avg `-0.0173` n `8`; equity avg `-0.0234` n `100`; fx avg `0.0036` n `6`; index avg `-0.0001` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0043` n `774`
- 1h: commodity avg `-0.0315` n `12`; crypto_alt avg `0.008` n `230`; crypto_major avg `0.067` n `8`; equity avg `0.0244` n `100`; fx avg `0.0056` n `6`; index avg `0.0037` n `25`; metal avg `-0.0149` n `20`; unknown avg `0.0001` n `774`
- 4h: commodity avg `-0.1044` n `12`; crypto_alt avg `0.1348` n `230`; crypto_major avg `0.2927` n `8`; equity avg `-0.0576` n `100`; fx avg `0.0321` n `6`; index avg `0.0076` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.135` n `774`
- 24h: commodity avg `-0.2409` n `12`; crypto_alt avg `-1.0365` n `230`; crypto_major avg `-0.8926` n `8`; equity avg `-2.9808` n `100`; fx avg `-0.0265` n `6`; index avg `-0.3118` n `25`; metal avg `0.0328` n `20`; unknown avg `14.0212` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1226`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1156`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1074`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1067`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
