# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T10:22:12.774295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1149` n `12`; crypto_alt avg `0.1315` n `228`; crypto_major avg `0.065` n `8`; equity avg `0.0572` n `67`; fx avg `0.0099` n `6`; index avg `-0.1475` n `23`; metal avg `-0.0201` n `18`; unknown avg `-0.3613` n `396`
- 1h: commodity avg `-0.1211` n `12`; crypto_alt avg `0.1761` n `228`; crypto_major avg `-0.0098` n `8`; equity avg `0.0574` n `67`; fx avg `0.0068` n `6`; index avg `-0.1681` n `23`; metal avg `-0.0604` n `18`; unknown avg `-0.4245` n `396`
- 4h: commodity avg `-0.1531` n `12`; crypto_alt avg `-1.6112` n `228`; crypto_major avg `-1.0859` n `8`; equity avg `-0.1541` n `67`; fx avg `-0.02` n `6`; index avg `-0.286` n `23`; metal avg `-0.0772` n `18`; unknown avg `-0.4455` n `386`
- 24h: commodity avg `-0.4119` n `12`; crypto_alt avg `-5.3016` n `228`; crypto_major avg `-3.8411` n `8`; equity avg `-1.5201` n `67`; fx avg `0.0467` n `6`; index avg `-0.3081` n `23`; metal avg `-1.0501` n `18`; unknown avg `-2.5508` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0464`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.044`, n `668`, weak_sample_signal
