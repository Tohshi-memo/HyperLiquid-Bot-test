# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T09:07:33.165534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `-0.1667` n `230`; crypto_major avg `-0.1019` n `8`; equity avg `0.0055` n `100`; fx avg `-0.0062` n `6`; index avg `-0.0063` n `25`; metal avg `0.0583` n `20`; unknown avg `-0.0345` n `775`
- 1h: commodity avg `-0.2141` n `12`; crypto_alt avg `-0.4007` n `230`; crypto_major avg `-0.1857` n `8`; equity avg `0.0567` n `100`; fx avg `-0.0005` n `6`; index avg `0.0296` n `25`; metal avg `0.0646` n `20`; unknown avg `-0.1033` n `775`
- 4h: commodity avg `-0.4949` n `12`; crypto_alt avg `-0.5392` n `230`; crypto_major avg `-0.2158` n `8`; equity avg `0.4714` n `100`; fx avg `0.0031` n `6`; index avg `0.0787` n `25`; metal avg `0.1611` n `20`; unknown avg `-0.0957` n `759`
- 24h: commodity avg `-0.9369` n `12`; crypto_alt avg `0.278` n `230`; crypto_major avg `1.0831` n `8`; equity avg `1.4525` n `100`; fx avg `0.1187` n `6`; index avg `0.196` n `25`; metal avg `0.4698` n `20`; unknown avg `-0.0726` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
