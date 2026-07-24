# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T15:37:29.212750+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.158` n `12`; crypto_alt avg `0.1014` n `230`; crypto_major avg `0.1206` n `8`; equity avg `0.1146` n `100`; fx avg `0.0082` n `6`; index avg `-0.0022` n `25`; metal avg `0.0236` n `20`; unknown avg `0.0283` n `773`
- 1h: commodity avg `-0.3688` n `12`; crypto_alt avg `0.5078` n `230`; crypto_major avg `0.5677` n `8`; equity avg `0.9537` n `100`; fx avg `0.0198` n `6`; index avg `0.1865` n `25`; metal avg `0.2108` n `20`; unknown avg `13.6458` n `773`
- 4h: commodity avg `-0.223` n `12`; crypto_alt avg `-0.6606` n `230`; crypto_major avg `-0.5349` n `8`; equity avg `-1.6542` n `100`; fx avg `0.0135` n `6`; index avg `-0.0807` n `25`; metal avg `0.1144` n `20`; unknown avg `13.1803` n `773`
- 24h: commodity avg `-0.7773` n `12`; crypto_alt avg `-1.3337` n `230`; crypto_major avg `-1.1031` n `8`; equity avg `-1.6237` n `100`; fx avg `-0.1153` n `6`; index avg `-0.0861` n `25`; metal avg `0.2268` n `20`; unknown avg `13.9012` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1453`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1175`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.117`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1036`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0999`, n `666`, weak_sample_signal
