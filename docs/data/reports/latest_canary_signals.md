# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T16:07:32.339115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0054` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `-0.0172` n `100`; fx avg `0.0168` n `6`; index avg `0.0088` n `25`; metal avg `0.0212` n `20`; unknown avg `0.0067` n `775`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `0.328` n `230`; crypto_major avg `0.168` n `8`; equity avg `0.0159` n `100`; fx avg `0.0037` n `6`; index avg `0.0054` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0212` n `775`
- 4h: commodity avg `0.0178` n `12`; crypto_alt avg `0.135` n `230`; crypto_major avg `0.2373` n `8`; equity avg `0.1044` n `100`; fx avg `-0.0007` n `6`; index avg `0.0225` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0041` n `775`
- 24h: commodity avg `-0.4529` n `12`; crypto_alt avg `1.1836` n `230`; crypto_major avg `1.3208` n `8`; equity avg `0.8723` n `100`; fx avg `0.0245` n `6`; index avg `0.1799` n `25`; metal avg `0.1767` n `20`; unknown avg `0.1439` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
