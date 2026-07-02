# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T09:37:29.022068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `0.5733` n `228`; crypto_major avg `0.7644` n `8`; equity avg `0.1212` n `88`; fx avg `-0.0103` n `6`; index avg `0.0135` n `25`; metal avg `0.0013` n `20`; unknown avg `0.0614` n `763`
- 1h: commodity avg `-0.1011` n `12`; crypto_alt avg `0.6155` n `228`; crypto_major avg `0.9571` n `8`; equity avg `0.1871` n `88`; fx avg `-0.0115` n `6`; index avg `-0.0085` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.1753` n `763`
- 4h: commodity avg `-0.1047` n `12`; crypto_alt avg `0.6707` n `228`; crypto_major avg `0.7442` n `8`; equity avg `-0.379` n `88`; fx avg `-0.0863` n `6`; index avg `-0.1144` n `25`; metal avg `0.1453` n `20`; unknown avg `2.3579` n `741`
- 24h: commodity avg `-0.4278` n `12`; crypto_alt avg `2.5846` n `228`; crypto_major avg `2.5007` n `8`; equity avg `-1.8252` n `88`; fx avg `-0.0954` n `6`; index avg `-0.5113` n `25`; metal avg `1.0843` n `20`; unknown avg `16.9816` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
