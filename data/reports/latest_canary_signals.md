# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T19:52:30.310490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0164` n `230`; crypto_major avg `-0.0723` n `8`; equity avg `-0.0336` n `98`; fx avg `-0.0054` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0215` n `20`; unknown avg `-0.0031` n `773`
- 1h: commodity avg `-0.0689` n `12`; crypto_alt avg `-0.1687` n `230`; crypto_major avg `-0.1846` n `8`; equity avg `-0.0017` n `98`; fx avg `-0.0114` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0353` n `20`; unknown avg `-0.0341` n `773`
- 4h: commodity avg `0.1537` n `12`; crypto_alt avg `-0.4523` n `230`; crypto_major avg `-0.3108` n `8`; equity avg `-0.6905` n `98`; fx avg `0.0032` n `6`; index avg `-0.0794` n `25`; metal avg `-0.2279` n `20`; unknown avg `0.0693` n `773`
- 24h: commodity avg `0.4959` n `12`; crypto_alt avg `-0.5916` n `230`; crypto_major avg `-0.7921` n `8`; equity avg `-0.7308` n `98`; fx avg `-0.0609` n `6`; index avg `-0.1512` n `25`; metal avg `0.232` n `20`; unknown avg `1.3843` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0914`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
