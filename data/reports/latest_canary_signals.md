# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T03:22:25.757763+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0537` n `13`; crypto_alt avg `-0.0662` n `239`; crypto_major avg `-0.1671` n `8`; equity avg `-0.3503` n `161`; fx avg `-0.0098` n `6`; index avg `-0.0381` n `27`; metal avg `-0.068` n `20`; unknown avg `0.2969` n `1262`
- 1h: commodity avg `-0.131` n `13`; crypto_alt avg `-0.3727` n `239`; crypto_major avg `-0.3723` n `8`; equity avg `-0.5372` n `161`; fx avg `-0.0652` n `6`; index avg `-0.0343` n `27`; metal avg `-0.0969` n `20`; unknown avg `21.4957` n `1254`
- 4h: commodity avg `-0.0748` n `13`; crypto_alt avg `0.5768` n `239`; crypto_major avg `0.4866` n `8`; equity avg `0.3945` n `161`; fx avg `-0.1234` n `6`; index avg `0.0294` n `27`; metal avg `0.0054` n `20`; unknown avg `22.1904` n `1250`
- 24h: commodity avg `0.0649` n `13`; crypto_alt avg `-1.9784` n `239`; crypto_major avg `-0.7054` n `8`; equity avg `0.9031` n `161`; fx avg `-0.2097` n `6`; index avg `0.0965` n `27`; metal avg `-0.448` n `20`; unknown avg `2.5342` n `1141`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
