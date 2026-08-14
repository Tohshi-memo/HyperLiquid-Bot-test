# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T08:52:30.803163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `-0.081` n `230`; crypto_major avg `-0.0063` n `8`; equity avg `-0.0264` n `113`; fx avg `0.0231` n `6`; index avg `0.0042` n `25`; metal avg `-0.0204` n `20`; unknown avg `0.0491` n `787`
- 1h: commodity avg `-0.0769` n `12`; crypto_alt avg `0.1128` n `230`; crypto_major avg `0.121` n `8`; equity avg `0.2667` n `113`; fx avg `-0.0199` n `6`; index avg `0.0326` n `25`; metal avg `-0.0143` n `20`; unknown avg `-0.0043` n `787`
- 4h: commodity avg `0.186` n `12`; crypto_alt avg `-0.3197` n `230`; crypto_major avg `-0.3163` n `8`; equity avg `0.3012` n `113`; fx avg `-0.0201` n `6`; index avg `0.0644` n `25`; metal avg `0.184` n `20`; unknown avg `0.0118` n `755`
- 24h: commodity avg `0.0314` n `12`; crypto_alt avg `-0.6154` n `230`; crypto_major avg `-0.6843` n `8`; equity avg `1.6929` n `113`; fx avg `-0.0631` n `6`; index avg `0.3364` n `25`; metal avg `-0.0879` n `20`; unknown avg `0.9155` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1798`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1606`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
