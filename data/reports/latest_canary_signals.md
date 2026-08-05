# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T12:52:36.243377+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0269` n `12`; crypto_alt avg `-0.1275` n `230`; crypto_major avg `-0.1855` n `8`; equity avg `-0.084` n `108`; fx avg `0.0064` n `6`; index avg `-0.0104` n `25`; metal avg `-0.1148` n `20`; unknown avg `0.037` n `782`
- 1h: commodity avg `0.0884` n `12`; crypto_alt avg `0.2073` n `230`; crypto_major avg `0.3061` n `8`; equity avg `0.1196` n `108`; fx avg `-0.0029` n `6`; index avg `0.0097` n `25`; metal avg `-0.1708` n `20`; unknown avg `0.119` n `782`
- 4h: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0256` n `230`; crypto_major avg `-0.0349` n `8`; equity avg `0.2659` n `108`; fx avg `-0.0013` n `6`; index avg `0.0645` n `25`; metal avg `0.0475` n `20`; unknown avg `0.6233` n `781`
- 24h: commodity avg `-0.2397` n `12`; crypto_alt avg `0.6401` n `230`; crypto_major avg `0.3623` n `8`; equity avg `2.0472` n `108`; fx avg `0.0585` n `6`; index avg `0.5612` n `25`; metal avg `0.5637` n `20`; unknown avg `0.0448` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
