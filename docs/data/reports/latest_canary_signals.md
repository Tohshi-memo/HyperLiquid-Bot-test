# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T03:22:33.051934+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.1822` n `234`; crypto_major avg `-0.277` n `8`; equity avg `-0.0236` n `141`; fx avg `0.0026` n `6`; index avg `-0.0054` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.0275` n `945`
- 1h: commodity avg `-0.0411` n `12`; crypto_alt avg `0.4135` n `234`; crypto_major avg `0.1028` n `8`; equity avg `-0.0048` n `141`; fx avg `0.0161` n `6`; index avg `-0.0063` n `26`; metal avg `0.0328` n `20`; unknown avg `1.7945` n `943`
- 4h: commodity avg `-0.0892` n `12`; crypto_alt avg `0.8265` n `234`; crypto_major avg `-0.1282` n `8`; equity avg `-0.2697` n `141`; fx avg `0.038` n `6`; index avg `-0.0497` n `26`; metal avg `-0.0554` n `20`; unknown avg `0.3929` n `937`
- 24h: commodity avg `0.4145` n `12`; crypto_alt avg `-4.4446` n `234`; crypto_major avg `-4.3017` n `8`; equity avg `-1.5274` n `140`; fx avg `0.1042` n `6`; index avg `-0.3162` n `26`; metal avg `-0.6116` n `20`; unknown avg `585.4285` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
