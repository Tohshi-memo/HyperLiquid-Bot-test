# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T02:37:24.882382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.2208` n `230`; crypto_major avg `0.1762` n `8`; equity avg `0.0311` n `114`; fx avg `-0.0024` n `6`; index avg `0.0036` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0292` n `792`
- 1h: commodity avg `0.0518` n `12`; crypto_alt avg `0.1528` n `230`; crypto_major avg `0.1079` n `8`; equity avg `0.1741` n `114`; fx avg `0.0128` n `6`; index avg `0.0168` n `25`; metal avg `-0.0034` n `20`; unknown avg `-0.0629` n `792`
- 4h: commodity avg `0.0368` n `12`; crypto_alt avg `0.8145` n `230`; crypto_major avg `1.0289` n `8`; equity avg `0.3098` n `114`; fx avg `-0.035` n `6`; index avg `0.0066` n `25`; metal avg `0.1853` n `20`; unknown avg `1.024` n `791`
- 24h: commodity avg `-0.0888` n `12`; crypto_alt avg `0.1942` n `230`; crypto_major avg `0.3101` n `8`; equity avg `0.5353` n `114`; fx avg `-0.054` n `6`; index avg `0.0537` n `25`; metal avg `0.2217` n `20`; unknown avg `-0.0109` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
