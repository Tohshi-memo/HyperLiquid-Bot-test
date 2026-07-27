# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T02:52:24.231883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0614` n `230`; crypto_major avg `-0.1579` n `8`; equity avg `-0.0375` n `100`; fx avg `-0.0072` n `6`; index avg `-0.0289` n `25`; metal avg `-0.0428` n `20`; unknown avg `0.6359` n `775`
- 1h: commodity avg `0.0338` n `12`; crypto_alt avg `0.0161` n `230`; crypto_major avg `-0.0651` n `8`; equity avg `0.3371` n `100`; fx avg `-0.0036` n `6`; index avg `0.016` n `25`; metal avg `-0.1245` n `20`; unknown avg `0.457` n `775`
- 4h: commodity avg `0.1142` n `12`; crypto_alt avg `-0.0775` n `230`; crypto_major avg `-0.4502` n `8`; equity avg `-0.2104` n `100`; fx avg `0.0936` n `6`; index avg `-0.1244` n `25`; metal avg `-0.0625` n `20`; unknown avg `-0.2773` n `775`
- 24h: commodity avg `-0.4582` n `12`; crypto_alt avg `1.3627` n `230`; crypto_major avg `1.1395` n `8`; equity avg `0.6718` n `100`; fx avg `0.1402` n `6`; index avg `0.0449` n `25`; metal avg `0.3516` n `20`; unknown avg `-0.0369` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
