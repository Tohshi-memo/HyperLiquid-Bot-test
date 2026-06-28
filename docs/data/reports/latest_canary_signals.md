# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T13:07:31.775504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.2881` n `228`; crypto_major avg `-0.3421` n `8`; equity avg `-0.0511` n `88`; fx avg `-0.0042` n `6`; index avg `-0.0029` n `23`; metal avg `-0.014` n `20`; unknown avg `-0.0543` n `764`
- 1h: commodity avg `-0.0462` n `12`; crypto_alt avg `-0.4347` n `228`; crypto_major avg `-0.4409` n `8`; equity avg `-0.0256` n `88`; fx avg `-0.0052` n `6`; index avg `-0.002` n `23`; metal avg `-0.0073` n `20`; unknown avg `-0.0381` n `764`
- 4h: commodity avg `0.0381` n `12`; crypto_alt avg `-0.517` n `228`; crypto_major avg `-0.4383` n `8`; equity avg `-0.0708` n `88`; fx avg `0.0024` n `6`; index avg `0.0032` n `23`; metal avg `-0.0104` n `20`; unknown avg `1.4561` n `750`
- 24h: commodity avg `0.134` n `12`; crypto_alt avg `-0.4482` n `228`; crypto_major avg `-1.0924` n `8`; equity avg `0.0096` n `88`; fx avg `-0.0028` n `6`; index avg `-0.0548` n `23`; metal avg `-0.0343` n `20`; unknown avg `15.5414` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
