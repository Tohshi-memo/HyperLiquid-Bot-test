# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T07:07:28.815454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0238` n `13`; crypto_alt avg `0.0875` n `238`; crypto_major avg `-0.0716` n `8`; equity avg `0.0459` n `156`; fx avg `-0.0102` n `6`; index avg `-0.0054` n `27`; metal avg `-0.0039` n `20`; unknown avg `1.8794` n `1258`
- 1h: commodity avg `-0.0598` n `13`; crypto_alt avg `-0.4964` n `238`; crypto_major avg `-0.5152` n `8`; equity avg `-0.1925` n `156`; fx avg `0.0415` n `6`; index avg `-0.0297` n `27`; metal avg `-0.0293` n `20`; unknown avg `3.6605` n `1256`
- 4h: commodity avg `-0.0375` n `13`; crypto_alt avg `-1.0072` n `238`; crypto_major avg `-0.7035` n `8`; equity avg `0.2534` n `156`; fx avg `0.0289` n `6`; index avg `0.0663` n `27`; metal avg `0.0994` n `20`; unknown avg `1.9772` n `1175`
- 24h: commodity avg `-0.4003` n `13`; crypto_alt avg `-1.7252` n `238`; crypto_major avg `-0.4043` n `8`; equity avg `1.07` n `156`; fx avg `0.2255` n `6`; index avg `0.3` n `27`; metal avg `0.1229` n `20`; unknown avg `3.1206` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
