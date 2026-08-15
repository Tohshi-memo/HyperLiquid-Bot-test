# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T10:37:22.893349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0015` n `12`; crypto_alt avg `-0.0525` n `230`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0055` n `114`; fx avg `-0.0012` n `6`; index avg `-0.0009` n `25`; metal avg `0.0011` n `20`; unknown avg `-0.0767` n `791`
- 1h: commodity avg `-0.02` n `12`; crypto_alt avg `0.038` n `230`; crypto_major avg `-0.0005` n `8`; equity avg `0.0134` n `114`; fx avg `-0.0098` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0159` n `791`
- 4h: commodity avg `-0.1006` n `12`; crypto_alt avg `0.0417` n `230`; crypto_major avg `-0.1376` n `8`; equity avg `0.0572` n `114`; fx avg `-0.0122` n `6`; index avg `0.0019` n `25`; metal avg `0.013` n `20`; unknown avg `-0.0084` n `791`
- 24h: commodity avg `-0.0396` n `12`; crypto_alt avg `1.0528` n `230`; crypto_major avg `0.078` n `8`; equity avg `-0.4946` n `114`; fx avg `0.1236` n `6`; index avg `-0.1363` n `25`; metal avg `0.2333` n `20`; unknown avg `-0.1376` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
