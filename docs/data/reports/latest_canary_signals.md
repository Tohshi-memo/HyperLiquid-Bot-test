# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:22:24.284800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0826` n `230`; crypto_major avg `0.0423` n `8`; equity avg `0.0274` n `114`; fx avg `-0.0144` n `6`; index avg `-0.0066` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.0391` n `791`
- 1h: commodity avg `-0.0094` n `12`; crypto_alt avg `0.0919` n `230`; crypto_major avg `0.0085` n `8`; equity avg `0.0438` n `114`; fx avg `-0.0141` n `6`; index avg `-0.0014` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.0457` n `791`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `0.1981` n `230`; crypto_major avg `0.1154` n `8`; equity avg `-0.0596` n `114`; fx avg `-0.0285` n `6`; index avg `0.0022` n `25`; metal avg `-0.0038` n `20`; unknown avg `-0.0049` n `791`
- 24h: commodity avg `0.0547` n `12`; crypto_alt avg `0.137` n `230`; crypto_major avg `0.1637` n `8`; equity avg `0.2707` n `114`; fx avg `-0.0267` n `6`; index avg `0.034` n `25`; metal avg `0.0388` n `20`; unknown avg `0.0681` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
