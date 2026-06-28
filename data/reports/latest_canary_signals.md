# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T20:07:32.565856+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.1255` n `228`; crypto_major avg `0.2541` n `8`; equity avg `0.0577` n `88`; fx avg `0.0165` n `6`; index avg `0.0009` n `23`; metal avg `-0.0021` n `20`; unknown avg `3.6159` n `764`
- 1h: commodity avg `0.0245` n `12`; crypto_alt avg `-0.2915` n `228`; crypto_major avg `-0.1733` n `8`; equity avg `0.0408` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0004` n `23`; metal avg `-0.0203` n `20`; unknown avg `2.9821` n `764`
- 4h: commodity avg `-0.0119` n `12`; crypto_alt avg `-1.2025` n `228`; crypto_major avg `-0.9471` n `8`; equity avg `-0.0407` n `88`; fx avg `-0.0207` n `6`; index avg `-0.022` n `23`; metal avg `0.0059` n `20`; unknown avg `2.7712` n `764`
- 24h: commodity avg `0.3629` n `12`; crypto_alt avg `-0.6425` n `228`; crypto_major avg `-1.0367` n `8`; equity avg `0.1415` n `88`; fx avg `-0.0312` n `6`; index avg `-0.0439` n `23`; metal avg `-0.014` n `20`; unknown avg `16.0203` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
