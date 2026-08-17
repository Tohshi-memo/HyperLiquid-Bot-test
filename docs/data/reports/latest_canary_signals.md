# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T12:07:28.043521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `12`; crypto_alt avg `-0.1656` n `230`; crypto_major avg `-0.1216` n `8`; equity avg `-0.1678` n `114`; fx avg `-0.0059` n `6`; index avg `-0.0262` n `25`; metal avg `-0.0283` n `20`; unknown avg `-0.0052` n `792`
- 1h: commodity avg `-0.0609` n `12`; crypto_alt avg `-0.1125` n `230`; crypto_major avg `-0.2507` n `8`; equity avg `-0.3094` n `114`; fx avg `-0.0015` n `6`; index avg `-0.0315` n `25`; metal avg `-0.0639` n `20`; unknown avg `0.0393` n `792`
- 4h: commodity avg `0.0536` n `12`; crypto_alt avg `-0.0678` n `230`; crypto_major avg `0.0201` n `8`; equity avg `-0.2686` n `114`; fx avg `0.0065` n `6`; index avg `-0.0303` n `25`; metal avg `-0.0614` n `20`; unknown avg `0.0145` n `792`
- 24h: commodity avg `-0.1357` n `12`; crypto_alt avg `-0.047` n `230`; crypto_major avg `0.7746` n `8`; equity avg `0.9688` n `114`; fx avg `-0.0194` n `6`; index avg `0.1205` n `25`; metal avg `0.1305` n `20`; unknown avg `0.0232` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
