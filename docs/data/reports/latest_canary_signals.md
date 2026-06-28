# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T17:07:27.992023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0449` n `12`; crypto_alt avg `0.1889` n `228`; crypto_major avg `0.353` n `8`; equity avg `0.0332` n `88`; fx avg `-0.0337` n `6`; index avg `0.0028` n `23`; metal avg `0.0053` n `20`; unknown avg `0.0431` n `764`
- 1h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.4355` n `228`; crypto_major avg `-0.2653` n `8`; equity avg `0.0362` n `88`; fx avg `-0.0245` n `6`; index avg `-0.0078` n `23`; metal avg `0.0111` n `20`; unknown avg `-0.2194` n `764`
- 4h: commodity avg `0.144` n `12`; crypto_alt avg `0.0988` n `228`; crypto_major avg `-0.0286` n `8`; equity avg `0.0683` n `88`; fx avg `-0.0292` n `6`; index avg `-0.011` n `23`; metal avg `-0.0386` n `20`; unknown avg `0.2277` n `764`
- 24h: commodity avg `0.4006` n `12`; crypto_alt avg `-0.6541` n `228`; crypto_major avg `-1.3272` n `8`; equity avg `0.1577` n `88`; fx avg `-0.0326` n `6`; index avg `-0.0417` n `23`; metal avg `-0.0672` n `20`; unknown avg `14.7881` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
