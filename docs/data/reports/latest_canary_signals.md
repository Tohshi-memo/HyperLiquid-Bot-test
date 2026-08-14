# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T20:51:01.550121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0228` n `12`; crypto_alt avg `-0.0099` n `230`; crypto_major avg `-0.0815` n `8`; equity avg `0.0187` n `114`; fx avg `-0.0033` n `6`; index avg `0.0011` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.1516` n `791`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `0.0162` n `230`; crypto_major avg `-0.068` n `8`; equity avg `0.0477` n `114`; fx avg `0.0131` n `6`; index avg `0.0111` n `25`; metal avg `-0.0293` n `20`; unknown avg `-0.0806` n `791`
- 4h: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1567` n `230`; crypto_major avg `-0.3238` n `8`; equity avg `0.1982` n `114`; fx avg `0.0199` n `6`; index avg `0.0403` n `25`; metal avg `-0.0639` n `20`; unknown avg `-0.4617` n `791`
- 24h: commodity avg `0.2027` n `12`; crypto_alt avg `0.2965` n `230`; crypto_major avg `-1.0265` n `8`; equity avg `-0.4185` n `114`; fx avg `0.0898` n `6`; index avg `-0.0803` n `25`; metal avg `0.2442` n `20`; unknown avg `-0.0309` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1568`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1532`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
