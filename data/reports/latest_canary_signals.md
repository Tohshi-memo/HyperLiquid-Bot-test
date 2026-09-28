# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T07:07:26.643781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0621` n `12`; crypto_alt avg `0.0437` n `234`; crypto_major avg `0.0515` n `8`; equity avg `0.0016` n `140`; fx avg `0.0101` n `6`; index avg `-0.0015` n `23`; metal avg `-0.1658` n `18`; unknown avg `0.3918` n `942`
- 1h: commodity avg `-0.0552` n `12`; crypto_alt avg `-0.4568` n `234`; crypto_major avg `-0.1892` n `8`; equity avg `-0.6139` n `141`; fx avg `-0.0241` n `6`; index avg `-0.0486` n `26`; metal avg `-0.1665` n `20`; unknown avg `1.2154` n `960`
- 4h: commodity avg `0.1137` n `12`; crypto_alt avg `-1.4626` n `234`; crypto_major avg `-0.9617` n `8`; equity avg `-0.8477` n `141`; fx avg `0.0165` n `6`; index avg `-0.0644` n `26`; metal avg `-0.2683` n `20`; unknown avg `1.3377` n `928`
- 24h: commodity avg `-0.3782` n `12`; crypto_alt avg `-2.873` n `234`; crypto_major avg `-2.2989` n `8`; equity avg `-2.2068` n `141`; fx avg `0.0681` n `6`; index avg `-0.2145` n `26`; metal avg `-0.9365` n `20`; unknown avg `4.1652` n `815`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
