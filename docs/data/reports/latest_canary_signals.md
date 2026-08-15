# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T07:37:30.904217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0539` n `12`; crypto_alt avg `-0.0653` n `230`; crypto_major avg `0.0062` n `8`; equity avg `-0.0103` n `114`; fx avg `0.0015` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0874` n `791`
- 1h: commodity avg `-0.1207` n `12`; crypto_alt avg `-0.0594` n `230`; crypto_major avg `-0.0376` n `8`; equity avg `0.061` n `114`; fx avg `-0.0047` n `6`; index avg `0.0167` n `25`; metal avg `0.0091` n `20`; unknown avg `0.0939` n `791`
- 4h: commodity avg `-0.1619` n `12`; crypto_alt avg `0.2364` n `230`; crypto_major avg `-0.1696` n `8`; equity avg `-0.0194` n `114`; fx avg `-0.029` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.0181` n `759`
- 24h: commodity avg `-0.2704` n `12`; crypto_alt avg `1.0248` n `230`; crypto_major avg `0.0637` n `8`; equity avg `-0.0741` n `114`; fx avg `0.1011` n `6`; index avg `-0.0598` n `25`; metal avg `0.2785` n `20`; unknown avg `-0.0636` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2157`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1771`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1751`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1576`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1472`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.142`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1418`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `669`, weak_sample_signal
