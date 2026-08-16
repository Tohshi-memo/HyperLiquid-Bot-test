# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T14:37:26.075225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0844` n `230`; crypto_major avg `0.0336` n `8`; equity avg `0.0043` n `114`; fx avg `0.0` n `6`; index avg `0.0012` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0318` n `791`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.0155` n `230`; crypto_major avg `0.074` n `8`; equity avg `0.0458` n `114`; fx avg `-0.0149` n `6`; index avg `-0.0055` n `25`; metal avg `0.0062` n `20`; unknown avg `-0.0328` n `791`
- 4h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.1107` n `230`; crypto_major avg `0.1455` n `8`; equity avg `-0.0592` n `114`; fx avg `-0.0285` n `6`; index avg `0.0053` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0615` n `791`
- 24h: commodity avg `0.0473` n `12`; crypto_alt avg `0.0314` n `230`; crypto_major avg `0.1675` n `8`; equity avg `0.264` n `114`; fx avg `-0.0269` n `6`; index avg `0.0405` n `25`; metal avg `0.0337` n `20`; unknown avg `0.0458` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1643`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
