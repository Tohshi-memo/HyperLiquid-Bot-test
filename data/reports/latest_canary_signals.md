# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T01:07:30.718913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0153` n `12`; crypto_alt avg `-0.2413` n `230`; crypto_major avg `-0.1403` n `8`; equity avg `-0.2216` n `102`; fx avg `-0.0076` n `6`; index avg `-0.0429` n `25`; metal avg `-0.1051` n `20`; unknown avg `0.2607` n `777`
- 1h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.3901` n `230`; crypto_major avg `-0.1526` n `8`; equity avg `-0.7365` n `102`; fx avg `-0.0314` n `6`; index avg `-0.1022` n `25`; metal avg `-0.1135` n `20`; unknown avg `0.1328` n `777`
- 4h: commodity avg `0.5902` n `12`; crypto_alt avg `-0.2283` n `230`; crypto_major avg `0.0261` n `8`; equity avg `0.1118` n `102`; fx avg `0.0076` n `6`; index avg `0.0914` n `25`; metal avg `-0.0875` n `20`; unknown avg `0.1078` n `776`
- 24h: commodity avg `-0.1645` n `12`; crypto_alt avg `0.6505` n `230`; crypto_major avg `1.1613` n `8`; equity avg `-1.119` n `102`; fx avg `-0.1535` n `6`; index avg `-0.0145` n `25`; metal avg `-0.2503` n `20`; unknown avg `0.3709` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
