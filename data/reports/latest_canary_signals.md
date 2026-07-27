# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T01:52:32.292693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0371` n `12`; crypto_alt avg `0.2444` n `230`; crypto_major avg `0.223` n `8`; equity avg `0.1701` n `100`; fx avg `0.0166` n `6`; index avg `0.0131` n `25`; metal avg `0.0691` n `20`; unknown avg `-0.1874` n `775`
- 1h: commodity avg `0.0777` n `12`; crypto_alt avg `-0.0066` n `230`; crypto_major avg `-0.1164` n `8`; equity avg `-0.5122` n `100`; fx avg `0.0313` n `6`; index avg `-0.1352` n `25`; metal avg `0.0087` n `20`; unknown avg `-0.1757` n `775`
- 4h: commodity avg `-0.1776` n `12`; crypto_alt avg `0.5412` n `230`; crypto_major avg `0.3754` n `8`; equity avg `-0.1404` n `100`; fx avg `0.0998` n `6`; index avg `-0.0219` n `25`; metal avg `0.2304` n `20`; unknown avg `-0.3547` n `775`
- 24h: commodity avg `-0.4954` n `12`; crypto_alt avg `1.4867` n `230`; crypto_major avg `1.3706` n `8`; equity avg `0.328` n `100`; fx avg `0.1484` n `6`; index avg `0.0264` n `25`; metal avg `0.4788` n `20`; unknown avg `0.0068` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
