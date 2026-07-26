# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T17:41:07.515364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `12`; crypto_alt avg `-0.0656` n `230`; crypto_major avg `-0.0877` n `8`; equity avg `-0.0229` n `100`; fx avg `-0.0005` n `6`; index avg `0.0091` n `25`; metal avg `-0.0046` n `20`; unknown avg `0.6896` n `775`
- 1h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.2453` n `230`; crypto_major avg `-0.2886` n `8`; equity avg `-0.0501` n `100`; fx avg `-0.0035` n `6`; index avg `0.005` n `25`; metal avg `-0.0232` n `20`; unknown avg `0.245` n `775`
- 4h: commodity avg `-0.0329` n `12`; crypto_alt avg `0.3782` n `230`; crypto_major avg `0.521` n `8`; equity avg `0.1228` n `100`; fx avg `-0.0172` n `6`; index avg `0.0394` n `25`; metal avg `0.0079` n `20`; unknown avg `0.1831` n `775`
- 24h: commodity avg `-0.3988` n `12`; crypto_alt avg `0.8122` n `230`; crypto_major avg `0.783` n `8`; equity avg `0.7397` n `100`; fx avg `0.0117` n `6`; index avg `0.1645` n `25`; metal avg `0.183` n `20`; unknown avg `0.0204` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1843`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
