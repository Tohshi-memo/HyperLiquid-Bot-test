# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T04:52:26.674564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0815` n `230`; crypto_major avg `-0.0592` n `8`; equity avg `0.0256` n `108`; fx avg `0.0344` n `6`; index avg `0.0008` n `25`; metal avg `-0.0325` n `20`; unknown avg `-0.0036` n `781`
- 1h: commodity avg `0.0873` n `12`; crypto_alt avg `0.1606` n `230`; crypto_major avg `0.06` n `8`; equity avg `0.0666` n `108`; fx avg `0.0451` n `6`; index avg `-0.0062` n `25`; metal avg `-0.002` n `20`; unknown avg `-0.0246` n `781`
- 4h: commodity avg `-0.0524` n `12`; crypto_alt avg `0.5777` n `230`; crypto_major avg `0.3986` n `8`; equity avg `0.5953` n `108`; fx avg `0.0322` n `6`; index avg `0.0163` n `25`; metal avg `0.3278` n `20`; unknown avg `-0.155` n `781`
- 24h: commodity avg `-1.4715` n `12`; crypto_alt avg `0.1562` n `230`; crypto_major avg `0.179` n `8`; equity avg `4.0088` n `108`; fx avg `0.0288` n `6`; index avg `0.8348` n `25`; metal avg `0.9806` n `20`; unknown avg `0.3597` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
