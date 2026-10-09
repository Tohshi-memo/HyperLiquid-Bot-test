# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T14:22:33.298006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0656` n `13`; crypto_alt avg `0.1622` n `235`; crypto_major avg `0.2519` n `8`; equity avg `-0.0547` n `150`; fx avg `-0.0108` n `6`; index avg `-0.0134` n `26`; metal avg `-0.0351` n `20`; unknown avg `-0.2141` n `1078`
- 1h: commodity avg `0.2381` n `13`; crypto_alt avg `-0.1468` n `235`; crypto_major avg `-0.0671` n `8`; equity avg `-0.6294` n `150`; fx avg `0.0123` n `6`; index avg `-0.0554` n `26`; metal avg `0.0516` n `20`; unknown avg `1.0887` n `1028`
- 4h: commodity avg `0.4424` n `13`; crypto_alt avg `-0.5447` n `235`; crypto_major avg `-0.1727` n `8`; equity avg `-0.6024` n `150`; fx avg `-0.0331` n `6`; index avg `-0.0831` n `26`; metal avg `0.051` n `20`; unknown avg `1.8932` n `1022`
- 24h: commodity avg `-0.217` n `13`; crypto_alt avg `-2.0857` n `235`; crypto_major avg `-1.3663` n `8`; equity avg `-0.841` n `150`; fx avg `0.0038` n `6`; index avg `-0.0826` n `26`; metal avg `0.5417` n `20`; unknown avg `1.0352` n `933`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
