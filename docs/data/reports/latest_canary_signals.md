# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T02:37:18.541605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0809` n `12`; crypto_alt avg `-0.3174` n `228`; crypto_major avg `-0.2311` n `8`; equity avg `-0.0333` n `67`; fx avg `-0.0049` n `6`; index avg `0.0644` n `23`; metal avg `-0.0396` n `18`; unknown avg `0.332` n `396`
- 1h: commodity avg `0.0557` n `12`; crypto_alt avg `-0.5706` n `228`; crypto_major avg `-0.4793` n `8`; equity avg `-0.0464` n `67`; fx avg `-0.0086` n `6`; index avg `0.0554` n `23`; metal avg `-0.0169` n `18`; unknown avg `0.3066` n `396`
- 4h: commodity avg `0.4476` n `12`; crypto_alt avg `-0.0733` n `228`; crypto_major avg `0.7172` n `8`; equity avg `0.3802` n `67`; fx avg `-0.0203` n `6`; index avg `0.5037` n `23`; metal avg `0.4274` n `18`; unknown avg `0.4005` n `396`
- 24h: commodity avg `-2.6419` n `12`; crypto_alt avg `1.7832` n `228`; crypto_major avg `2.3235` n `8`; equity avg `2.1851` n `67`; fx avg `0.039` n `6`; index avg `1.2045` n `23`; metal avg `1.143` n `18`; unknown avg `1.6542` n `376`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
