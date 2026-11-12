# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T08:22:26.749511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0492` n `13`; crypto_alt avg `-0.0244` n `239`; crypto_major avg `-0.0702` n `8`; equity avg `0.0075` n `161`; fx avg `-0.0042` n `6`; index avg `0.0117` n `27`; metal avg `-0.0281` n `20`; unknown avg `0.0023` n `1262`
- 1h: commodity avg `0.1077` n `13`; crypto_alt avg `-0.1508` n `239`; crypto_major avg `0.0165` n `8`; equity avg `0.1372` n `161`; fx avg `0.0323` n `6`; index avg `0.0194` n `27`; metal avg `0.0388` n `20`; unknown avg `16.864` n `1238`
- 4h: commodity avg `0.4479` n `13`; crypto_alt avg `-0.3999` n `239`; crypto_major avg `-0.3427` n `8`; equity avg `-0.575` n `161`; fx avg `0.0969` n `6`; index avg `-0.0986` n `27`; metal avg `-0.0651` n `20`; unknown avg `17.7515` n `1202`
- 24h: commodity avg `0.4642` n `13`; crypto_alt avg `-1.7214` n `239`; crypto_major avg `-0.921` n `8`; equity avg `-0.769` n `161`; fx avg `-0.0764` n `6`; index avg `-0.0855` n `27`; metal avg `-0.632` n `20`; unknown avg `17.2005` n `1125`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
