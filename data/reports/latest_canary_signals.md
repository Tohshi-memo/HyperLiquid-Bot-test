# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T19:34:22.218913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.0302` n `230`; crypto_major avg `0.0091` n `8`; equity avg `0.1045` n `114`; fx avg `0.0015` n `6`; index avg `0.0126` n `25`; metal avg `0.029` n `20`; unknown avg `0.0363` n `791`
- 1h: commodity avg `-0.0732` n `12`; crypto_alt avg `-0.1784` n `230`; crypto_major avg `-0.0957` n `8`; equity avg `0.0582` n `114`; fx avg `0.0091` n `6`; index avg `0.0189` n `25`; metal avg `0.0166` n `20`; unknown avg `8.674` n `791`
- 4h: commodity avg `-0.0185` n `12`; crypto_alt avg `0.2848` n `230`; crypto_major avg `-0.3504` n `8`; equity avg `0.0596` n `114`; fx avg `0.0116` n `6`; index avg `0.0259` n `25`; metal avg `0.0017` n `20`; unknown avg `18.5468` n `791`
- 24h: commodity avg `0.1872` n `12`; crypto_alt avg `0.1827` n `230`; crypto_major avg `-1.0911` n `8`; equity avg `-0.55` n `114`; fx avg `0.0772` n `6`; index avg `-0.0785` n `25`; metal avg `0.2419` n `20`; unknown avg `0.0421` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
