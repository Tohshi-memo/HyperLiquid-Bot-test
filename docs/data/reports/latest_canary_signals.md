# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T02:37:18.672409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0748` n `12`; crypto_alt avg `-0.1207` n `228`; crypto_major avg `-0.2417` n `8`; equity avg `-0.0161` n `67`; fx avg `0.0051` n `6`; index avg `-0.0086` n `23`; metal avg `0.0223` n `18`; unknown avg `-0.0362` n `396`
- 1h: commodity avg `-0.1202` n `12`; crypto_alt avg `-0.0772` n `228`; crypto_major avg `-0.3084` n `8`; equity avg `0.0737` n `67`; fx avg `0.0139` n `6`; index avg `-0.016` n `23`; metal avg `-0.1276` n `18`; unknown avg `0.3145` n `396`
- 4h: commodity avg `-0.1552` n `12`; crypto_alt avg `0.5959` n `228`; crypto_major avg `0.0268` n `8`; equity avg `0.2437` n `67`; fx avg `-0.1436` n `6`; index avg `0.1118` n `23`; metal avg `0.1879` n `18`; unknown avg `0.3335` n `396`
- 24h: commodity avg `0.2297` n `12`; crypto_alt avg `-0.9449` n `228`; crypto_major avg `-0.0023` n `8`; equity avg `0.256` n `67`; fx avg `-0.0353` n `6`; index avg `-0.2526` n `23`; metal avg `0.6244` n `18`; unknown avg `-0.4879` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
