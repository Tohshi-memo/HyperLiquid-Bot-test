# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T12:52:27.729655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0745` n `230`; crypto_major avg `-0.0728` n `8`; equity avg `-0.0172` n `100`; fx avg `0.0006` n `6`; index avg `-0.0092` n `25`; metal avg `0.0201` n `20`; unknown avg `0.0237` n `775`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.0161` n `230`; crypto_major avg `0.0127` n `8`; equity avg `-0.0713` n `100`; fx avg `0.0075` n `6`; index avg `-0.0078` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0914` n `775`
- 4h: commodity avg `-0.2863` n `12`; crypto_alt avg `0.009` n `230`; crypto_major avg `0.0206` n `8`; equity avg `0.213` n `100`; fx avg `0.0113` n `6`; index avg `0.0448` n `25`; metal avg `0.1129` n `20`; unknown avg `-0.0435` n `775`
- 24h: commodity avg `-0.8416` n `12`; crypto_alt avg `1.4589` n `230`; crypto_major avg `1.5617` n `8`; equity avg `0.7068` n `100`; fx avg `0.0271` n `6`; index avg `0.1704` n `25`; metal avg `0.1926` n `20`; unknown avg `0.1194` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1899`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
